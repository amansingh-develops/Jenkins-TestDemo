package com.exam;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class App {
    public static final int PORT = 8081;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);
        
        server.createContext("/", new FormHandler());
        server.createContext("/register", new RegistrationHandler());

        server.setExecutor(null);
        System.out.println("Student Registration Server started on http://localhost:" + PORT);
        server.start();
    }

    static class FormHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            File htmlFile = new File("index.html");
            byte[] bytes;
            if (htmlFile.exists()) {
                FileInputStream fis = new FileInputStream(htmlFile);
                bytes = fis.readAllBytes();
                fis.close();
            } else {
                bytes = "<h1>Student Registration Form</h1>".getBytes(StandardCharsets.UTF_8);
            }
            exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
            exchange.sendResponseHeaders(200, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }
    }

    static class RegistrationHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "<!DOCTYPE html><html><body style='font-family:Arial;text-align:center;padding:50px;'>"
                    + "<h2 style='color:green;'>Registration Successful!</h2>"
                    + "<p>Student registration details recorded successfully.</p>"
                    + "<a href='/'>Go back</a></body></html>";
            byte[] bytes = response.getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
            exchange.sendResponseHeaders(200, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }
    }
}
