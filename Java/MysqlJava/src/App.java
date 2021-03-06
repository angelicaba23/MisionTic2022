/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author angel
 */
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author angel
 */
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.DriverManager;
/**
 *
 */
public class App {

    /**
     * @param args the command line arguments
     * @throws java.sql.SQLException
     */
    
    public static final String URL = "jdbc:mysql://localhost/centromedico";
    public static final String USER = "root";
    public static final String CLAVE = "";
    
    
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        // TODO code application logic here

        Connection connection;        
        
        try { 

            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = (Connection) DriverManager.getConnection(URL, USER, CLAVE);          
            
            Statement statement = connection.createStatement();
            statement.executeUpdate("drop table if exists medicos");
            statement.executeUpdate("create table medicos (idMedico int(11), mednombres varchar(100), medapellidos varchar(100))");
            statement.executeUpdate("insert into medicos values(1, 'NombreMedico1', 'ApellidoMedico1')");
            statement.executeUpdate("insert into medicos values(2, 'NombreMedico2', 'ApellidoMedico2')");
            
            
            String sql;
            sql = "SELECT * FROM medicos";
            ResultSet rs = statement.executeQuery(sql);
            
            while (rs.next()) {
                // read the result set
                System.out.println("idMedico = " + rs.getInt("idMedico"));
                System.out.println("nombres = " + rs.getString("mednombres"));
                System.out.println("apellidos = " + rs.getString("medapellidos"));
            }
            

            //------------------------------------------
            statement.executeUpdate("drop table if exists persona");
            statement.executeUpdate("create table persona (cedula int(11), nombre varchar(100))");
            statement.executeUpdate("insert into persona values(1, 'Jhon')");
            statement.executeUpdate("insert into persona values(2, 'Patricia')");

            PreparedStatement ps = connection.prepareStatement("insert into persona values(?, ?)");
            ps.setInt(1, 3);
            ps.setString(2, "Pedro");
            ps.executeUpdate();

            ResultSet consulta = statement.executeQuery("SELECT * FROM persona where cedula = 2");
            while (consulta.next()) {
                // read the result set
                System.out.print("C??dula = " + consulta.getInt("cedula"));
                System.out.println(", Nombre = " + consulta.getString("nombre"));

            }

            statement.executeUpdate("DELETE FROM persona WHERE cedula = 2");
            statement.executeUpdate("UPDATE persona SET nombre = 'Julian Cardona' WHERE cedula = 1");

            ResultSet consulta1 = statement.executeQuery("SELECT * FROM persona");
            while (consulta1.next()) {
                // read the result set
                System.out.print("C??dula = " + consulta1.getInt("cedula"));
                System.out.println(", Nombre = " + consulta1.getString("nombre"));

            }
        } catch (SQLException e) {
            // TODO: handle exception
            System.err.println(e.getClass().getName() + ":" + e.getMessage());
            System.out.println("Error en la conexi??n");
        }

    }

}
