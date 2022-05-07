#Candidato - Eduardo Kleber Santos Silva
#Lakewood
#classificação - 3
#dia de semana  normais/reward - R$110/R$80
#final de semana  normais/reward - R$90/R$80

#Bridgewood
#classificação - 4
#dia de semana  normais/reward - R$160/R$110
#final de semana  normais/reward - R$60/R$50  

#Ridgewood
#classificação - 5
#dia de semana  normais/reward - R$220/R$100
#final de semana  normais/reward - R$150/R$40 


data = str(input('Quais as datas para reserva? (Digite com a formatação correta DD/MM/AA): '))
dia = str(input('Qual o dia da semana?:'))

if dia == "Sabado"  :
    print('Final de semana!')
elif dia == "Domingo":
    print('Final de semana!')
elif dia == "domingo":
    print('Final de semana!')
elif dia == "sabado":
    print('Final de semana!')
else:
    print('Dia útil!')

plano = str(input('Faz parte do plano fidelidade?: '))


if plano == 'Sim':
    plano = "Reward"
    print('Olá, você faz parte do plano fidelidade, então temos alguns descontos para você!')
else:
    plano = "Regular"
    print('Por ficar de fora do nosso plano fidelidade você perderá alguns descontos!')

num = 0
while num != 3:
    print('''    [1] Escolher pelo melhor preço para dias úteis
    [2] Escolher pelas melhores avaliações
    [3] Escolher pelo melhor preço no fim de semana
    [4] Para cancelar''')
    num = int(input('Qual sua escolha?'))
    if num==1:
        nome=(str(input('\nDigite o nome do escolhido:'
                        '\nLakewood - R$110,00 / R$80,00 para usuários do plano fidelidade '
                        '\nBridgewood - R$160,00 / R$110,00 para usuários do plano fidelidade'
                        '\nRidgwood - R$220,00 / R$100,00 para usuário do plano fidelidade ----:')))
        print(f'{plano}: O {nome} foi o selecionado por ter o melhor preço para o usuário, venha fazer o check-in em {data}!')
        break
    elif num==2:
        nome=(str(input('---------Melhores avalições-------'
                        '\nRidgewood - Classificação - 5'
                        '\nBridgewood - Classificação - 4'
                        '\nLakewood - Classificação - 3 ------:')))
        print(f'{plano}: O {nome} foi o selecionado por ter a melhor avaliação para o usuário, venha fazer o check-in em {data}!')
        break
    elif num==3:
        nome=(str(input('Melhores preços no fim de semana (Digite o escolhido no final)'
                        '\nLakewood - R$90,00 / R$80,00 para usuários do plano fidelidade '
                        '\nBridgewood - R$60,00 / R$50,00 para usuários do plano fidelidade'
                        '\nRidgwood - R$150,00 / R$40,00 para usuário do plano fidelidade ----:')))
        print(f'{plano}: O {nome} foi o selecionado pelo melhor preço, venha fazer o check-in em {data}!')
        break
    elif num==4:
       print("Até mais!")
       break
    print('Saindo da seleção...')







