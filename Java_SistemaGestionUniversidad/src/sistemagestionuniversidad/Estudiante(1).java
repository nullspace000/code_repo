
package sistemagestionuniversidad;

public class Estudiante extends MiembroUniversidad{
    public int semestre;
    public String grupo;
    
    //constructor estudiante
    public Estudiante(int id,String nombre,int edad,int semestre,String grupo){
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.semestre = semestre;
        this.grupo = grupo;
        System.out.println("Construyendo instancia de Estudiante "+nombre);
    }
    
    //método actualizar datos Estudiante
    public void actualizarDatosEstudiante(int edad,int semestre,String grupo){
        this.edad = edad;
        this.semestre = semestre;
        this.grupo = grupo;
        System.out.println("Actualizando datos de estudiante "+this.nombre+".");
    }
    
    
    //método mostrar datos Estudiante
    public void mostrarDatosEstudiante(){
        System.out.println("id: "+this.id);
        System.out.println("Nombre: "+this.nombre);
        System.out.println("Edad: "+this.edad);
        System.out.println("Semestre: "+this.semestre);
        System.out.println("Grupo: "+this.grupo);
    }
}
