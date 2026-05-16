"""
Database module for user tracking and progress persistence
Uses SQLite for simple, scalable storage that works on Streamlit Cloud
"""

import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path
import pandas as pd

# Database file location
DB_PATH = Path(__file__).parent.parent / "data" / "app.db"

# Ensure data directory exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def init_database():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            created_date TEXT NOT NULL,
            last_accessed TEXT,
            total_sessions INTEGER DEFAULT 0,
            total_score REAL DEFAULT 0
        )
    """)

    # Quiz sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_sessions (
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            quiz_type TEXT NOT NULL,
            topic TEXT,
            start_time TEXT NOT NULL,
            end_time TEXT,
            score INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            accuracy REAL DEFAULT 0,
            confidence_avg REAL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    # Answers table - stores individual question answers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            question_text TEXT,
            user_answer TEXT,
            correct_answer TEXT,
            is_correct BOOLEAN,
            confidence INTEGER,
            difficulty TEXT,
            concept TEXT,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (session_id) REFERENCES quiz_sessions(session_id)
        )
    """)

    conn.commit()
    conn.close()


def get_or_create_user(name: str) -> int:
    """
    Get existing user by name or create new user
    Returns: user_id
    """
    if not name or not name.strip():
        return None

    name = name.strip()
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Try to get existing user
    cursor.execute("SELECT user_id FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        # Update last_accessed
        cursor.execute(
            "UPDATE users SET last_accessed = ? WHERE user_id = ?",
            (datetime.now().isoformat(), user_id)
        )
        conn.commit()
        conn.close()
        return user_id

    # Create new user
    cursor.execute(
        "INSERT INTO users (name, created_date, last_accessed) VALUES (?, ?, ?)",
        (name, datetime.now().isoformat(), datetime.now().isoformat())
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id


def get_user_by_id(user_id: int) -> dict:
    """Get user details by ID"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, name, created_date, last_accessed, total_sessions, total_score
        FROM users WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            'user_id': result[0],
            'name': result[1],
            'created_date': result[2],
            'last_accessed': result[3],
            'total_sessions': result[4],
            'total_score': result[5]
        }
    return None


def get_all_users() -> list:
    """Get list of all users"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, name, created_date, total_sessions, total_score
        FROM users ORDER BY last_accessed DESC
    """)

    results = cursor.fetchall()
    conn.close()

    users = []
    for row in results:
        users.append({
            'user_id': row[0],
            'name': row[1],
            'created_date': row[2],
            'total_sessions': row[3],
            'total_score': row[4]
        })
    return users


def create_quiz_session(user_id: int, quiz_type: str, topic: str = None) -> int:
    """
    Create a new quiz session
    Returns: session_id
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_sessions
        (user_id, quiz_type, topic, start_time)
        VALUES (?, ?, ?, ?)
    """, (user_id, quiz_type, topic, datetime.now().isoformat()))

    conn.commit()
    session_id = cursor.lastrowid
    conn.close()
    return session_id


def save_answer(session_id: int, question_id: str, question_text: str,
                user_answer: str, correct_answer: str, is_correct: bool,
                confidence: int = 3, difficulty: str = "medium", concept: str = "") -> None:
    """
    Save a single answer to the database
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO answers
        (session_id, question_id, question_text, user_answer, correct_answer,
         is_correct, confidence, difficulty, concept, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (session_id, question_id, question_text, user_answer, correct_answer,
          is_correct, confidence, difficulty, concept, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def end_quiz_session(session_id: int, score: int, total_questions: int,
                     accuracy: float, confidence_avg: float = 3.0) -> None:
    """
    Mark quiz session as complete and update stats
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Update session
    cursor.execute("""
        UPDATE quiz_sessions
        SET end_time = ?, score = ?, total_questions = ?, accuracy = ?, confidence_avg = ?
        WHERE session_id = ?
    """, (datetime.now().isoformat(), score, total_questions, accuracy, confidence_avg, session_id))

    # Get user_id to update user stats
    cursor.execute("SELECT user_id FROM quiz_sessions WHERE session_id = ?", (session_id,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        # Update user total sessions and score
        cursor.execute("""
            UPDATE users
            SET total_sessions = total_sessions + 1, total_score = total_score + ?
            WHERE user_id = ?
        """, (score, user_id))

    conn.commit()
    conn.close()


def get_user_sessions(user_id: int) -> list:
    """Get all quiz sessions for a user"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT session_id, quiz_type, topic, start_time, end_time,
               score, total_questions, accuracy
        FROM quiz_sessions
        WHERE user_id = ?
        ORDER BY start_time DESC
    """, (user_id,))

    results = cursor.fetchall()
    conn.close()

    sessions = []
    for row in results:
        sessions.append({
            'session_id': row[0],
            'quiz_type': row[1],
            'topic': row[2],
            'start_time': row[3],
            'end_time': row[4],
            'score': row[5],
            'total_questions': row[6],
            'accuracy': row[7]
        })
    return sessions


def get_session_answers(session_id: int) -> list:
    """Get all answers from a quiz session"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT answer_id, question_id, question_text, user_answer,
               correct_answer, is_correct, confidence, difficulty, concept, timestamp
        FROM answers
        WHERE session_id = ?
        ORDER BY timestamp ASC
    """, (session_id,))

    results = cursor.fetchall()
    conn.close()

    answers = []
    for row in results:
        answers.append({
            'answer_id': row[0],
            'question_id': row[1],
            'question_text': row[2],
            'user_answer': row[3],
            'correct_answer': row[4],
            'is_correct': row[5],
            'confidence': row[6],
            'difficulty': row[7],
            'concept': row[8],
            'timestamp': row[9]
        })
    return answers


def get_user_performance_by_difficulty(user_id: int) -> dict:
    """
    Get performance breakdown by difficulty level
    Returns: {'easy': {'total': X, 'correct': Y}, 'medium': {...}, 'hard': {...}}
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT difficulty, COUNT(*) as total, SUM(is_correct) as correct
        FROM answers
        WHERE session_id IN (
            SELECT session_id FROM quiz_sessions WHERE user_id = ?
        )
        GROUP BY difficulty
    """, (user_id,))

    results = cursor.fetchall()
    conn.close()

    performance = {}
    for row in results:
        difficulty = row[0] or "unknown"
        total = row[1]
        correct = row[2] or 0
        performance[difficulty] = {
            'total': total,
            'correct': correct,
            'accuracy': round((correct / total * 100), 1) if total > 0 else 0
        }
    return performance


def get_user_performance_by_concept(user_id: int) -> dict:
    """
    Get performance breakdown by concept/topic
    Returns: {'Water': {'total': X, 'correct': Y}, ...}
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT concept, COUNT(*) as total, SUM(is_correct) as correct
        FROM answers
        WHERE session_id IN (
            SELECT session_id FROM quiz_sessions WHERE user_id = ?
        )
        GROUP BY concept
        ORDER BY total DESC
    """, (user_id,))

    results = cursor.fetchall()
    conn.close()

    performance = {}
    for row in results:
        concept = row[0] or "General"
        total = row[1]
        correct = row[2] or 0
        performance[concept] = {
            'total': total,
            'correct': correct,
            'accuracy': round((correct / total * 100), 1) if total > 0 else 0
        }
    return performance


def get_user_weak_areas(user_id: int, top_n: int = 5) -> list:
    """
    Get questions the user answered incorrectly
    Returns: list of incorrect answers sorted by recency
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT question_text, user_answer, correct_answer, concept, timestamp
        FROM answers
        WHERE session_id IN (
            SELECT session_id FROM quiz_sessions WHERE user_id = ?
        ) AND is_correct = 0
        ORDER BY timestamp DESC
        LIMIT ?
    """, (user_id, top_n))

    results = cursor.fetchall()
    conn.close()

    weak_areas = []
    for row in results:
        weak_areas.append({
            'question': row[0],
            'user_answer': row[1],
            'correct_answer': row[2],
            'concept': row[3],
            'timestamp': row[4]
        })
    return weak_areas


def get_user_stats(user_id: int) -> dict:
    """Get comprehensive stats for a user"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Total stats
    cursor.execute("""
        SELECT COUNT(*) as total_questions,
               SUM(is_correct) as correct_answers,
               AVG(CAST(is_correct AS FLOAT)) as avg_accuracy,
               AVG(confidence) as avg_confidence
        FROM answers
        WHERE session_id IN (
            SELECT session_id FROM quiz_sessions WHERE user_id = ?
        )
    """, (user_id,))

    result = cursor.fetchone()
    total_questions = result[0] or 0
    correct_answers = result[1] or 0
    avg_accuracy = round(result[2] * 100, 1) if result[2] else 0
    avg_confidence = round(result[3], 1) if result[3] else 0

    # Session stats
    cursor.execute("""
        SELECT COUNT(*) as total_sessions,
               AVG(accuracy) as avg_session_accuracy
        FROM quiz_sessions
        WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    total_sessions = result[0] or 0
    avg_session_accuracy = round(result[1], 1) if result[1] else 0

    conn.close()

    return {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'overall_accuracy': avg_accuracy,
        'avg_confidence': avg_confidence,
        'total_sessions': total_sessions,
        'avg_session_accuracy': avg_session_accuracy
    }


def export_user_data_csv(user_id: int) -> str:
    """
    Export user's quiz data as CSV string
    Returns: CSV content as string
    """
    conn = sqlite3.connect(str(DB_PATH))

    # Get sessions
    sessions_df = pd.read_sql("""
        SELECT session_id, quiz_type, topic, start_time, end_time, score, total_questions, accuracy
        FROM quiz_sessions
        WHERE user_id = ?
        ORDER BY start_time DESC
    """, conn, params=(user_id,))

    # Get answers
    answers_df = pd.read_sql("""
        SELECT a.*
        FROM answers a
        WHERE a.session_id IN (
            SELECT session_id FROM quiz_sessions WHERE user_id = ?
        )
        ORDER BY a.timestamp ASC
    """, conn, params=(user_id,))

    conn.close()

    # Create CSV with both
    output = "=== SESSIONS ===\n"
    output += sessions_df.to_csv(index=False)
    output += "\n\n=== DETAILED ANSWERS ===\n"
    output += answers_df.to_csv(index=False)

    return output


def delete_user_data(user_id: int) -> None:
    """Delete a user and all their data (careful!)"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Get all session IDs for this user
    cursor.execute("SELECT session_id FROM quiz_sessions WHERE user_id = ?", (user_id,))
    sessions = cursor.fetchall()

    # Delete answers for these sessions
    for session in sessions:
        cursor.execute("DELETE FROM answers WHERE session_id = ?", (session[0],))

    # Delete sessions
    cursor.execute("DELETE FROM quiz_sessions WHERE user_id = ?", (user_id,))

    # Delete user
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

    conn.commit()
    conn.close()
