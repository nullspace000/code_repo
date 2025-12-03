package sistemagestionuniversidad;

public class MiembroUniversidad extends SistemaGestionUniversidad{
    public int id;
    public String nombre;
    public int edad;
    
    //getters de todos los miembros
    public void mostrarId(){
        System.out.println("id: "+this.id);
    }
    
    public void mostrarNombre(){
        System.out.println("Nombre: "+this.nombre);
    }
    
    public void mostrarEdad(){
        System.out.println("Edad: "+this.edad);
    }
    
    public String getNombre(){
        return this.nombre;
    }
}
