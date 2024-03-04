soma = 0

# Feito à mão para não se perder

for mil in (0,1):
    if mil == 1:
        soma += 3

    for centena in range(10):

        if centena == 1:
            soma += 3

        elif centena == 2:
            soma += 8

        elif centena == 3:
            soma += 9 

        elif centena == 4:
            soma += 12

        elif centena == 5:
            soma += 10

        elif centena == 6:
            soma += 10

        elif centena == 7:
            soma += 10

        elif centena == 8:
            soma += 10

        elif centena == 9:
            soma += 10

        for dezena in range(10):

            if centena == 1:
                soma += 3

            elif centena == 2:
                soma += 5

            elif centena == 3:
                soma += 6

            elif centena == 4:
                soma += 8

            elif centena == 5:
                soma += 9

            elif centena == 6:
                soma += 8

            elif centena == 7:
                soma += 7

            elif centena == 8:
                soma += 7

            elif centena == 9:
                soma += 7

            for unidade in range(10):

                if centena == 1:
                    soma += 2

                elif centena == 2:
                    soma += 4

                elif centena == 3:
                    soma += 4

                elif centena == 4:
                    soma += 6

                elif centena == 5:
                    soma += 5

                elif centena == 6:
                    soma += 4

                elif centena == 7:
                    soma += 4

                elif centena == 8:
                    soma += 4

                elif centena == 9:
                    soma += 4

print(soma)