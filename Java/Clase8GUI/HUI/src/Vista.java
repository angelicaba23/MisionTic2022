import javax.swing.*;

public class Vista extends JFrame{

    public JTextField campo1 = new JTextField(10);
    public JLabel etiqueta1 = new JLabel("+");
    public JTextField campo2 = new JTextField(10);
    public JButton btnSumar = new JButton("Sumar");
    public JTextField rta = new JTextField(10);

    public Vista(){
        JPanel panelCalculator = new JPanel();
        
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500,300);
        
        panelCalculator.add(campo1);
        panelCalculator.add(etiqueta1);
        panelCalculator.add(campo2);
        panelCalculator.add(btnSumar);
        panelCalculator.add(rta);

        this.add(panelCalculator);        
    }

    public int getCampo1() {
        return Integer.parseInt(campo1.getText());
    }

    public int getCampo2() {
        return Integer.parseInt(campo2.getText());
    }
    
    public void setRta(int n){
        rta.setText(Integer.toString(n));
    }

    public void mostraMsg(String msg){
        JOptionPane.showMessageDialog(this,msg);
    }
}