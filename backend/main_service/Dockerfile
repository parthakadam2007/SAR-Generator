FROM eclipse-temurin:25-jre

WORKDIR /app

# ENV DB_URL=jdbc:postgresql://aws-1-ap-south-1.pooler.supabase.com:6543/postgres?user=postgres.iravjtmvujenyrlqngsw&password=SAR_Generator@password

COPY target/main_service-0.0.1-SNAPSHOT.jar app.jar

EXPOSE 8080

ENTRYPOINT [ "java" , "-jar" ,"app.jar" ]