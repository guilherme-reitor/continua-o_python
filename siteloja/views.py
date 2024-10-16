from django.shortcuts import render
from .utils import criptografia
from .models import Clientes

def cadcli(request):


    if request.method == 'POST':
        codcli = request.POST.get('codcli')
        nome  = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        senhacripto = criptografia(senha)

        cliente =  Clientes(
            codcli = codcli,
            nome = nome,
            cpf = cpf,
            email = email,
            senha = senhacripto
        )

        cliente.save()

        return render(request,'formcli.html')

    return render(request,'formcli.html')

