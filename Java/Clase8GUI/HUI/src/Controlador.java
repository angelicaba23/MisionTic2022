import java.awt.event.*;

public class Controlador implements ActionListener {
    private Vista vista;
    private Modelo modelo;

    public Controlador(Vista vista, Modelo modelo) {
        this.vista = vista;
        this.modelo = modelo;
        this.vista.btnSumar.addActionListener(this);
    }

    public void iniciar(){
        vista.setTitle("MVC");
        vista.setLocationRelativeTo(null);
    }

    public void actionPerformed(ActionEvent evt){
        try{
            modelo.setNumOne(vista.getCampo1());
            modelo.setNumTwo(Integer.parseInt(vista.campo2.getText()));
            modelo.sumar();
            vista.rta.setText(String.valueOf(modelo.getResult()));
        }catch(NumberFormatException e){
            vista.mostraMsg("Deben ser numeros");
        }
    }
    

}