FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/student-registration-1.0-SNAPSHOT.jar app.jar
COPY index.html index.html
EXPOSE 8081
ENTRYPOINT ["java", "-jar", "app.jar"]
