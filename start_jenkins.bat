@echo off
title Jenkins CI Server
echo ===================================================
echo Starting Jenkins CI Server on http://localhost:8080
echo ===================================================
echo.
cd /d "C:\Users\Asus\jenkins"
if not exist "jenkins.war" (
    echo Error: jenkins.war not found in C:\Users\Asus\jenkins
    pause
    exit /b 1
)
java -jar jenkins.war --httpPort=8080
pause
