import java.awt.HeadlessException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.JOptionPane;

public class Conexion {
    Connection conectar = null;
    String usuario = "root";
    String contrasena = "Root1234";
    String baseDatos = "db_java";
    String ip = "localhost";
    String puerto = "3306";

    String cadena = "jdbc:mysql://"+ip+":"+puerto+"/"+baseDatos+"?useSSL=false&serverTimezone=UTC";

    public Connection estableConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conectar = DriverManager.getConnection(cadena, usuario, contrasena);
            JOptionPane.showMessageDialog(null, "Conectado a la base de datos");
            
        } catch (HeadlessException | ClassNotFoundException | SQLException e) {
            JOptionPane.showMessageDialog(null, "No se conecto a la base de datos: " + e.toString());
        }
        return conectar;
    }
}
