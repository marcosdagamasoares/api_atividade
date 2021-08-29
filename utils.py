from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Marcos", idade=61)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    #pessoa = Pessoas.query.filter_by(nome="Marcos").first()
    pessoa = Pessoas.query.all()
    print(pessoa)
    #print(pessoa.nome, pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Marcos").first()
    pessoa.idade = 20
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Marcos").first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclui_pessoa()
    consulta_pessoas()
