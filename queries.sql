-- Eligible Students
SELECT s.student_id, s.name, sp.codekata_score, sp.career_track_score
FROM students s
JOIN student_performance sp ON s.student_id = sp.student_id
WHERE sp.codekata_score >= ? AND sp.career_track_score >= ?;

-- Average CodeKata
SELECT AVG(codekata_score) FROM student_performance;

-- Top Students
SELECT s.name, (sp.codekata_score + sp.career_track_score) AS total_score
FROM students s
JOIN student_performance sp ON s.student_id = sp.student_id
ORDER BY total_score DESC
LIMIT 5;

-- Placement Distribution
SELECT placement_status, COUNT(*) 
FROM placements
GROUP BY placement_status;

-- Performance vs Placement
SELECT placement_status, 
       AVG(codekata_score), 
       AVG(career_track_score)
FROM student_performance sp
JOIN placements p ON sp.student_id = p.student_id
GROUP BY placement_status;

-- Softskill vs Placement
 SELECT p.placement_status,
           AVG(ss.communication_score) AS avg_communication_score,
           AVG(ss.teamwork_score) AS avg_teamwork_score
           FROM placements p
           JOIN soft_skills ss 
           ON p.student_id = ss.student_id
           GROUP BY p.placement_status;