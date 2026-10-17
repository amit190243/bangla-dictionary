package com.abd;

import com.abd.database.DatabaseConnection;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;

import java.sql.Connection;
import java.sql.SQLException;

public class App extends Application {

    @Override
    public void start(Stage stage) {

        try (Connection connection = DatabaseConnection.connect()) {

            System.out.println("Database connected successfully.");
            System.out.println("Database URL: " + connection.getMetaData().getURL());

        } catch (SQLException e) {
            System.err.println("Database connection failed.");
            e.printStackTrace();
        }

        Label label = new Label("Bangla Dictionary");

        Scene scene = new Scene(label, 500, 300);

        stage.setTitle("Bangla Dictionary");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
