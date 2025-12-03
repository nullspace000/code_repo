
package sistemagestionuniversidad;

public class Profesor extends MiembroUniversidad{
    public String materia;
    private double sueldo;
    public String nivelEducacion;
    
    //constructor Profesor
    public Profesor(int id,String nombre,int edad,String materia,double sueldo,
            String nivelEducacion){
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.materia = materia;
        this.sueldo = sueldo;
        this.nivelEducacion = nivelEducacion;
    }
    
    //mostrar sueldo
    public void mostrarSueldoProfesor(){
        System.out.println("Sueldo por hora: "+this.sueldo);
    }
    
    //getSueldo
    public double getSueldo(){
        return this.sueldo;
    }
    
    //actualizar datos
    public void actualizarDatosProfesor(int edad,String materia,double sueldo,
            String nivelEducacion){
        this.edad = edad;
        this.materia = materia;
        this.sueldo = sueldo;
        this.nivelEducacion = nivelEducacion;
        System.out.println("Actualizando datos de profesor "+this.nombre+".");
    }

    //mostrar datos
    public void mostrarDatosProfesor(){
        System.out.println("id: "+this.id);
        System.out.println("Nombre: "+this.nombre);
        System.out.println("Edad: "+this.edad);
        System.out.println("Materia: "+this.materia);
        System.out.println("Sueldo: "+this.sueldo);
        System.out.println("Nivel de educacion: "+this.nivelEducacion);
    }
}
