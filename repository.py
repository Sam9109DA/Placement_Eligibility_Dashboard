from database import DatabaseConnection

class StudentRepository:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

        if self.cursor is None:
            print(" Cursor not created. DB connection failed.")
        else:
            print(" Cursor ready:", self.cursor)

    def get_all_students(self):
        query = "SELECT * FROM students"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM students WHERE student_id = ?"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchone() 
    
    def get_eligible_students(self, min_codekata, min_ct):
        query = """
        SELECT s.student_id, s.name, sp.codekata_score, sp.career_track_score
        FROM students s
        JOIN student_performance sp
        ON s.student_id = sp.student_id
        WHERE sp.codekata_score >= ?
        AND sp.career_track_score >= ?
        """
        self.cursor.execute(query, (min_codekata, min_ct))
        return self.cursor.fetchall()
    
    def total_students(self):
        query = "SELECT COUNT(*) FROM students"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    def get_eligibility_percentage(self):
        query = """
    SELECT 
        (COUNT(CASE 
            WHEN codekata_score >= 50 AND career_track_score >= 50 
            THEN 1 
        END) * 100.0 / COUNT(*)) AS eligibility_percentage
        FROM student_performance;
                """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return round(result[0], 2) if result[0] is not None else 0
    
    def get_avg_codekata(self):
        query = "SELECT AVG(codekata_score) FROM student_performance"
        self.cursor.execute(query)
        return round(self.cursor.fetchone()[0], 2)
    
    def get_top_students(self):
        query = """
        SELECT s.name, (sp.codekata_score + sp.career_track_score) AS total_score
        FROM students s
        JOIN student_performance sp ON s.student_id = sp.student_id
        ORDER BY total_score DESC
        LIMIT 5;
    """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_placement_distribution(self):
        query = """
       SELECT placement_status, COUNT(*) 
       FROM placements
       GROUP BY placement_status;
    """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_performance_vs_placement(self):
        query = """
       SELECT p.placement_status, 
           AVG(sp.codekata_score) AS avg_codekata,
           AVG(sp.career_track_score) AS avg_ct
           FROM placements p
           JOIN student_performance sp 
           ON p.student_id = sp.student_id
         GROUP BY p.placement_status;
    """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_softskills_vs_placement(self):
       query = """
       SELECT p.placement_status,
           AVG(ss.communication_score) AS avg_communication_score,
           AVG(ss.teamwork_score) AS avg_teamwork_score
           FROM placements p
           JOIN soft_skills ss 
           ON p.student_id = ss.student_id
           GROUP BY p.placement_status;
    """
       self.cursor.execute(query)
       return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()