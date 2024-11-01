from empresa import Empresa
from empleado import Empleado

print('*** Sistema de Empleados ***')

# Creamos una instancia de empresa
empresa1 = Empresa('Acme Inc.')
empresa1.contratar_empleados('Federico', 'Ventas')
empresa1.contratar_empleados('Juan', 'Ventas')
empresa1.contratar_empleados('Javier', 'Marketing')
empresa1.contratar_empleados('Alma', 'RRHH')

# Obtener el total de objetos de tipo empleados
print(f'Total de empleados: {Empleado.get_total_empleados()}')

# Obtener el numero de empleados en el dep de Ventas
print(f'Numero de empleados en el departamento de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')
empresa1.obtener_total_empleados()