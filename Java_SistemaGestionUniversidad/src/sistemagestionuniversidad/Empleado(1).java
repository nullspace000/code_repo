
package sistemagestionuniversidad;

public class Empleado extends MiembroUniversidad{
    public String puesto;
    private double sueldo;
    public String nivelEducacion;
    
    //constructor empleado
    public Empleado(int id,String nombre,int edad,String puesto,double sueldo,
            String nivelEducacion){
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.puesto = puesto;
        this.sueldo = sueldo;
        this.nivelEducacion = nivelEducacion;
        System.out.println("Construyendo instancia de Empleado "+this.nombre);
    }
    
    //actualizar información
    public void actualizarInfoEmpleado(int edad,String puesto,double sueldo,
            String nivelEducacion){
        this.edad = edad;
        this.puesto = puesto;
        this.sueldo = sueldo;
        this.nivelEducacion = nivelEducacion;
        System.out.println("Actualizando datos de empleado "+this.nombre+".");
    }
    
    //getSueldo
    public double getSueldo(){
        return this.sueldo;
    }
    
    //método mostrar infromación
    public void mostrarDatosEmpleado(){
        System.out.println("ID: "+this.id);
        System.out.println("Nombre: "+this.nombre);
        System.out.println("Edad: "+this.edad);
        System.out.println("Puesto: "+this.puesto);
        System.out.println("Sueldo: "+this.sueldo);
        System.out.println("Nivel de educacion: "+this.nivelEducacion);
    }
}

