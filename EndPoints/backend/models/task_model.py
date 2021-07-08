from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    

##################################################


    def get_courses(self):  
        rv = self.mysql_pool.execute("SELECT * from cursos")  
        data = []
        content = {}
        for result in rv:
            content = {'Curso': result[0]}
            data.append(content)
            content = {}
        return data

    def add_course(self, Nombre):    
        params = {
            'Nombre' : Nombre
        }  
        query = """INSERT INTO cursos (Nombre) 
            values (%(Nombre)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True) 
        cursor.lastrowid

        data = {'Nombre': Nombre}
        return data

    def delete_course(self, Nombre):    
        params = {'Nombre' : Nombre}      
        query = """delete from cursos where Nombre = %(Nombre)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'Delete': 1}
        return data


##################################################


    def get_groups(self):  
        rv = self.mysql_pool.execute("SELECT * from grupos")  
        data = []
        content = {}
        for result in rv:
            content = {'Grupo': result[0]}
            data.append(content)
            content = {}
        return data

    def add_group(self, Grupo):    
        params = {
            'Grupo' : Grupo
        }  
        query = """INSERT INTO grupos (Grupo) 
            values (%(Grupo)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True) 
        cursor.lastrowid

        data = {'Grupo': Grupo}
        return data

    def delete_group(self, Grupo):    
        params = {'Grupo' : Grupo}      
        query = """delete from grupos where Grupo = %(Grupo)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'Delete': 1}
        return data


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.delete_task(67))
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))
