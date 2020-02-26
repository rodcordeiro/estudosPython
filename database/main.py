from decouple import config
import MySQLdb


def connect():
    db = MySQLdb.connect(passwd=config("DB_PASSWORD"), db=config("DB_NAME"),
                    user=config("DB_USER"), host=config("DB_HOST"))
    cursor = db.cursor()
    query = "select * from testes;"
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado








def teste():
    mensagem = "/subscribeTag Java,Python,Javascript,Ruby on Rails, java script"
    tags = mensagem[14:]
    for tag in tags.split(","):
        tag = tag.lower()
        tag = tag.title()
        tag = tag.replace(" ","")
        for dado in list(connect()):
            print(dado)
            if tag in dado:
                query = f"INSERT INTO subscribed_tag(id_user,{dado[0]})"
            else:
                query = f"""INSERT INTO tag(tag,status) value({tag},'pendente')"""
        print(tag)




teste()
