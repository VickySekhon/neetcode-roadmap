select
CASE
     when A = B then "Isoceles"
     when A <> B then "Scalene"
     when A > B then "Equilateral"
END
FROM Grades;

