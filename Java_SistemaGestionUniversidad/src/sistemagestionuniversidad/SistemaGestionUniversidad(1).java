package sistemagestionuniversidad;
import java.util.Scanner;

public class SistemaGestionUniversidad {
    

    public static void main(String[] args) {
        
        Scanner scannerStrings = new Scanner(System.in);
        Scanner scannerInts = new Scanner(System.in);
        Scanner scannerDoubles = new Scanner(System.in);
        
        //variables temporales miembrosUniversidad
        String nombreTemporal;
        int idTemporal;
        int edadTemporal;

        //variables temporales estudiantes
        int semestreTemporal;
        String grupoTemporal;
        //arreglo de estudiantes
        Estudiante estudiantes[] = new Estudiante[100];
        //índice del arreglo estudiantes[] para ir guardando a los nuevos estudiantes
        int estudiantesIndex = 0;
        int y = 0;
        
        //variables temporales profesores
        String materiaTemporal;
        double sueldoTemporal;
        String nivelEducacionTemporal;
        double horasTemporales;
        double sueldoSemanal;
        //arreglo profesores
        Profesor profesores[] = new Profesor[100];
        int profesoresIndex = 0;
        
        
        //variables temporales empleados
        String puestoTemporal;
        //arreglo empleados
        Empleado empleados[] = new Empleado[100];
        int empleadosIndex = 0;
        
        //construcción de instancias de referencia
            //estudiante diego couto
            estudiantes[estudiantesIndex] = new Estudiante(estudiantesIndex, "Diego Couto", 19, 1, "24A");
            //estudiantes[estudiantesIndex] = nuevoEstudiante; me acabo de dar cuenta de que la variable nuevoEstudiante no es necesaria >:(
            estudiantesIndex++;
            System.out.println("Estudiante Diego Couto ha sido registrad@...");
            //estudiante sofia rosas
            estudiantes[estudiantesIndex] = new Estudiante(estudiantesIndex, "Sofía Rosas", 20, 2, "27D");
            estudiantesIndex++;
            System.out.println("Estudiante Sofia Rosas ha sido registrad@...");
            //estudiante fabian marques
            estudiantes[estudiantesIndex] = new Estudiante(estudiantesIndex, "Fabian Marques", 22, 4, "18A");
            estudiantesIndex++;
            System.out.println("Estudiante Fabian Marques ha sido registrad@...");
            //estudiante marcos castillos
            estudiantes[estudiantesIndex] = new Estudiante(estudiantesIndex, "Marcos Castillos", 24, 8, "32C");
            estudiantesIndex++;
            System.out.println("Estudiante Marcos Castillos ha sido registrad@...");
            
            //profesor Michael Hammer
            profesores[profesoresIndex] = new Profesor(profesoresIndex,"Michael Hammer",42,"Ciberseguridad",1400,"Maestria");
            profesoresIndex++;
            System.out.println("Profesor Michael Hammer ha sido registrad@...");
            //profesor robertos salinas
            profesores[profesoresIndex] = new Profesor(profesoresIndex,"Roberto Salinas",33,"Ciencias de datos",700,"Maestria");
            profesoresIndex++;
            System.out.println("Profesor Roberto Salinasha sido registrad@...");
            //profesor Javier Ortega
            profesores[profesoresIndex] = new Profesor(profesoresIndex,"Javier Ortega",54,"Desarollo back-end",1700,"Doctorado");
            profesoresIndex++;
            System.out.println("Profesor Javier Ortega ha sido registrad@...");
            //profesora Ana Aguilar
            profesores[profesoresIndex] = new Profesor(profesoresIndex,"Ana Aguilar",39,"Conputacion en la nube",1200,"Maestria");
            profesoresIndex++;
            System.out.println("Profesor Ana Aguilar ha sido registrad@...");
            
            //empleados
            empleados[empleadosIndex] = new Empleado(empleadosIndex,"Maria Sanches",27,"contadora",1000,"Licenciatura");
            empleadosIndex++;
            System.out.println("Emplead@ Maria Sanches ha sido registrad@...");
            
            empleados[empleadosIndex] = new Empleado(empleadosIndex, "Saul Quinta",30,"Administrador de red",1000,"Licenciatura");
            empleadosIndex++;
            System.out.println("Emplead@ Saul Quinta ha sido registrad@...");
            
            empleados[empleadosIndex] = new Empleado(empleadosIndex,"Tadeo Desont",45,"Director General",2000,"Maestria");
            empleadosIndex++;
            System.out.println("Emplead@ Tadeo Desont ha sido registrad@...");
            
            empleados[empleadosIndex] = new Empleado(empleadosIndex,"Gustavo Dias",26,"Mentor",1000,"Licenciatura");
            empleadosIndex++;
            System.out.println("Empleado Gustavo Dias ha sido registrad@...");
                    
        System.out.println("");
        System.out.println("Bienvenido usuario.");        
        boolean continuar = true;
        while(continuar == true){
            
            int operacion = 0;
            System.out.println("Ingrese el numero corespondiente a la operacion "
                    + "que desea realizar:");
            System.out.println("======================================");            
            System.out.println("0. Cerrar programa");
            System.out.println("1. Registrar nuevo estudiante");
            System.out.println("2. Actualizar datos de estudiante");
            System.out.println("3. Mostrar datos de estudiante");
            System.out.println("4. Imprimir lista de estudiantes");
            System.out.println("--------------------------------------");
            
            System.out.println("5. Registrar nuevo profesor");
            System.out.println("6. Actualizar datos de profesor");
            System.out.println("7. Mostrar datos de profesor");
            //ingresar numero de horas para calcular el sueldo del profesor
            System.out.println("8. Calcular sueldo semanal de profesor");            
            System.out.println("9. Imprimir lista de profesores");
            System.out.println("--------------------------------------");
            
            System.out.println("10. Registrar nuevo empleado");
            System.out.println("11. Actualizar datos de empleado");
            System.out.println("12. Mostrar datos de empleado");
            System.out.println("13. Calcular sueldo semanal de empleado");
            System.out.println("14. Imprimir lista empleados");
            System.out.println("======================================");
            
            try{
                operacion = scannerInts.nextInt();
            }catch(Exception e){
                System.out.println("Error: Dato invalido...");
            }
            switch(operacion){
                case 0: //cerrar programa
                    System.out.println("Cerrando programa...");
                    continuar = false; //rompe el bucle
                    break;
            
            //casos estudiantes
                case 1: //bloque para registrar nuevo estudiante
                    System.out.println("Ingrese el nombre del estudiante: ");
                    //try{
                    nombreTemporal = scannerStrings.nextLine();
                    //}catch(Exception e){
                    //    System.out.println("Error: Dato invalido...");
                    //}
                    idTemporal = estudiantesIndex;
                    System.out.println("Ingrese la edad del estudiante: ");
                    //try{
                    edadTemporal = scannerInts.nextInt();
                    //}catch(Exception e){
                    //    System.out.println("Error: Dato invalido...");
                    //}
                    System.out.println("Ingrese el semestre que cursa el estudiante: ");
                    //try{
                    semestreTemporal = scannerInts.nextInt();
                    //}catch(Exception e){
                    //    System.out.println("Error: Dato invalido...");
                    //}
                    System.out.println("Ingrese el grupo del estudiante: ");
                    //try{
                    grupoTemporal = scannerStrings.nextLine();
                    //}catch(Exception e){
                    //    System.out.println("Error: Dato invalido...");
                    //}
                    
                    estudiantes[estudiantesIndex] = new Estudiante(idTemporal, nombreTemporal, 
                            edadTemporal, semestreTemporal, grupoTemporal);
                    estudiantes[estudiantesIndex].mostrarDatosEstudiante();
                    estudiantesIndex++;//aumenta cada vez que asinamos un estudiante al index acual del arreglo estudiantes[]

                    System.out.println("Estudiante "+nombreTemporal+" ha sido "
                            + "registrad@...");
                    System.out.println("");
                    break;
                
                
                case 2:
                    //bloque para actualizar los datos de un estudiante
                    System.out.println("Ingrese el id del estudiante: ");
                    idTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la edad actual del estudiante "
                            +estudiantes[idTemporal].getNombre()+": ");
                    edadTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese el semestre actual que cursa el estudiante: ");
                    semestreTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese el grupo actual del estudiante: ");
                    grupoTemporal = scannerStrings.nextLine();
                    
                    estudiantes[idTemporal].actualizarDatosEstudiante(edadTemporal, 
                            semestreTemporal, grupoTemporal);
                    System.out.println("Los datos del estudiante han sido actualizados...");
                    estudiantes[idTemporal].mostrarDatosEstudiante();
                    System.out.println("");
                    break;
                            
                case 3:
                    //bloque mostrar datos de estudiante
                    System.out.println("Ingrese el id del estudiante: ");
                    idTemporal = scannerInts.nextInt();
                    estudiantes[idTemporal].mostrarDatosEstudiante();
                    System.out.println("");
                    break;
                    
                case 4:
                    //bloque imprimir lista de estudiantes
                    y = 0;
                    System.out.println("Imprimiendo lista de estudiantes: ");
                    for(int i = 0; i < estudiantesIndex;i++){
                        System.out.println(y +". "+estudiantes[y].getNombre());
                        y++;    
                    }
                    System.out.println("");
                    break;
                    
            //casos profesores
                case 5:
                    //bloque registrar nuevo profesor
                    System.out.println("Ingrese el nombre del profesor: ");
                    nombreTemporal = scannerStrings.nextLine();
                    idTemporal = profesoresIndex;
                    System.out.println("Ingrese la edad del profesor: ");
                    edadTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la materia que imparte el profesor: ");
                    materiaTemporal = scannerStrings.nextLine();
                    System.out.println("Ingrese el sueldo por hora del profesor: ");
                    sueldoTemporal = scannerDoubles.nextDouble();
                    System.out.println("Ingrese el nivel de educacion del profesor:");
                    nivelEducacionTemporal = scannerStrings.nextLine();
                    
                    profesores[profesoresIndex] = new Profesor(idTemporal,nombreTemporal,edadTemporal, materiaTemporal,sueldoTemporal, nivelEducacionTemporal);
                    profesores[profesoresIndex].mostrarDatosProfesor();
                    profesoresIndex++;//aumenta cada vez que asinamos un estudiante al index acual del arreglo estudiantes[]

                    System.out.println("Profesor "+nombreTemporal+" ha sido registrad@...");
                    System.out.println("");
                    break;
                    
                case 6:
                    //bloque para actualizar datos de profesor
                    System.out.println("Ingrese el id del profesor: ");
                    idTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la edad actual del profesor "+profesores[idTemporal].getNombre()+": ");
                    edadTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la materia que imparte el profesor actualmente: ");
                    materiaTemporal = scannerStrings.nextLine();
                    System.out.println("Ingrese el sueldo por hora actual del profesor: ");
                    sueldoTemporal = scannerDoubles.nextDouble();
                    System.out.println("Ingrese el nivel de educacion actual del profesor: ");
                    nivelEducacionTemporal = scannerStrings.nextLine();
                    
                    profesores[idTemporal].actualizarDatosProfesor(edadTemporal,materiaTemporal,sueldoTemporal,nivelEducacionTemporal);
                    System.out.println("Los datos del profesor han sido actualizados...");
                    System.out.println("");
                    profesores[idTemporal].mostrarDatosProfesor();
                    break;
                    
                    
                case 7:
                    //bloque para mostrar datos del profesor
                    System.out.println("Ingrese el id del profesor: ");
                    idTemporal = scannerInts.nextInt();
                    profesores[idTemporal].mostrarDatosProfesor();
                    System.out.println("");
                    break;

                    
                case 8:
                    //bloque para calcular el sueldo semanal del profesor
                    System.out.println("Ingrese el id del profesor: ");
                    idTemporal = scannerInts.nextInt();
                    sueldoTemporal = profesores[idTemporal].getSueldo();
                    System.out.println("Ingrese las horas de clase que imparte el profesor "+profesores[idTemporal].getNombre()+" por semana: ");
                    horasTemporales = scannerDoubles.nextDouble();
                    sueldoSemanal = horasTemporales * sueldoTemporal;
                    System.out.println("El salario semanal del profesor "+profesores[idTemporal].getNombre()+" que imparte "+horasTemporales+" horas de clase por semana, es de: "+sueldoSemanal);
                    System.out.println("");
                    break;
                    
                case 9:
                    //listar profesores
                    y = 0;
                    System.out.println("Imprimiendo lista de profesores: ");
                    for(int i = 0; i < profesoresIndex;i++){
                        System.out.println(y +". "+profesores[y].getNombre());
                        y++;
                    }
                    System.out.println("");
                    break;
                             
            //casos para empleados        
                case 10:
                    //registrar nuevo empleado
                    System.out.println("Ingrese el nombre del empleado: ");
                    nombreTemporal = scannerStrings.nextLine();
                    idTemporal = empleadosIndex;
                    System.out.println("Ingrese la edad del empleado: ");
                    edadTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese el puesto del empleado: ");
                    puestoTemporal = scannerStrings.nextLine();
                    System.out.println("Ingrese el sueldo por hora del empleado: ");
                    sueldoTemporal = scannerDoubles.nextDouble();
                    System.out.println("Ingrese el nivel de educacion del empleado:");
                    nivelEducacionTemporal = scannerStrings.nextLine();
                    
                    empleados[empleadosIndex] = new Empleado(idTemporal, nombreTemporal, edadTemporal, puestoTemporal, sueldoTemporal, nivelEducacionTemporal);
                    empleados[empleadosIndex].mostrarDatosEmpleado();
                    empleadosIndex++;//aumenta cada vez que asinamos un estudiante al index acual del arreglo estudiantes[]

                    System.out.println("Empleado "+nombreTemporal+" ha sido registrad@...");
                    System.out.println("");
                    break;
                    
                case 11:
                    //actulizar datos empleado
                    System.out.println("Ingrese el id del empleado: ");
                    idTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la edad actual del empleado"+empleados[idTemporal].getNombre()+": ");
                    edadTemporal = scannerInts.nextInt();
                    System.out.println("Ingrese la materia que imparte el profesor actualmente: ");
                    materiaTemporal = scannerStrings.nextLine();
                    System.out.println("Ingrese el sueldo por hora actual del profesor: ");
                    sueldoTemporal = scannerDoubles.nextDouble();
                    System.out.println("Ingrese el nivel de educacion actual del profesor: ");
                    nivelEducacionTemporal = scannerStrings.nextLine();
                    
                    profesores[idTemporal].actualizarDatosProfesor(edadTemporal,materiaTemporal,sueldoTemporal,nivelEducacionTemporal);
                    System.out.println("Los datos del estudiante han sido actualizados...");
                    estudiantes[idTemporal].mostrarDatosEstudiante();
                    System.out.println("");
                    break;
                    
                case 12:
                    //mostrar datos empleado
                    System.out.println("Ingrese el id del empleado: ");
                    idTemporal = scannerInts.nextInt();
                    empleados[idTemporal].mostrarDatosEmpleado();
                    System.out.println("");
                    break;
                    
                case 13:
                    //calcular sueldo semanal 
                    System.out.println("Ingrese el id del empleado: ");
                    idTemporal = scannerInts.nextInt();
                    sueldoTemporal = empleados[idTemporal].getSueldo();
                    System.out.println("Ingrese el numero de horas que trabaja el empleado "+empleados[idTemporal].getNombre()+" por semana: ");
                    horasTemporales = scannerDoubles.nextDouble();
                    sueldoSemanal = horasTemporales * sueldoTemporal;
                    System.out.println("El salario semanal del profesor "+profesores[idTemporal].getNombre()+" que imparte "+horasTemporales+" horas de clase por semana, es de: "+sueldoSemanal);
                    System.out.println("");
                    break;
                    
                case 14:
                    //imprimir lista empleados
                    y = 0;
                    System.out.println("Imprimiendo lista de empleados: ");
                    for(int i = 0; i < empleadosIndex;i++){
                        System.out.println(y +". "+empleados[y].getNombre());
                        y++;
                    }
                    System.out.println("");
                    break;
            }
        }
        
    }
    
}
