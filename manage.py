import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""INSERT INTO usuarios
               (id,email, senha) VALUES
               (1,'felippecardoso54@gmail.com','roseli23')
               """)
conexao.commit()
conexao.close()

print("Iserido com sucesso!")