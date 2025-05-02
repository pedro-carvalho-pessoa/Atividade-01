# Atividade-01
....
01. 


    #include <stdio.h>

    char main()
    {

    char comida[100];
    
    printf("Digite uma palavra da sua escolha: ");
    scanf("%s", &comida);
    printf("A palavra escolhida foi %s", comida);
    return 0;
    }
    ###############################################################

02            

    #include <stdio.h>
    
    int main()

    {
    int a,b;
    printf("Informe um número: ");
    scanf("%d",&a);
    printf("Informe outro número: ");
    scanf("%d",&b);
    printf("A multiplicação entre eles será de %d", a*b);
    return 0;
    }
###############################################################

03.  

    #include <stdio.h>

    int main()

    {
    
    int a,b;
    printf("Informe um número: ");
    scanf("%d",&a);
    if(a%2==0){
        printf("O número %d é par", a);
    }
    else{
        printf("O número %d é ímpar", a);
    }
    return 0;
    }
###############################################################


04.    

    #include <stdio.h>

    int main()
    
    {
    
    int a,b;
    printf("Informe um número: ");
    scanf("%d",&a);
    printf("Informe outro número: ");
    scanf("%d",&b);
    if(a > b){
        printf("O número %d é maior", a);
    }
    if(b > a){
        printf("O número %d é maior", b);
    }
    if(a==b){
        printf("Os números são iguais");
    }
    return 0;
    }
###############################################################
6. 

    #include <stdio.h>

    int main()

    {
    
    int a,contador;
    printf("Informe um número: ");
    scanf("%d",&a);
    contador=1;
    while(contador < 11){
        printf("\n%d x %d = %d",a,contador, a*contador);
        contador += 1;
    }
    }
###############################################################
7.  

    #include <stdio.h>

    float main()

    {
    
    float a,media,contador, valortotal;
    media=0;
    contador=1;
    printf("Informe sua nota: ");
    scanf("%f",&a);
    if(a>=0){
        media = a;
        while(contador < 3){
            printf("Informe sua nota: ");
            scanf("%f",&a);
            media += a;
            contador +=1;
        }
        valortotal= media/3;
        if(media >=7){
        printf("Aprovado! Sua média foi %.1f", valortotal);
        }
        else{
            printf("Reprovado! Sua média foi %.1f", valortotal);
        }   
    }
    else{
        printf("Informe um valor positivo para a média");
    }
    }
###############################################################
07. 

    #include <stdio.h>

    char main()
    {

    char nome[100];
    printf("Digite seu nome: ");
    scanf("%s", &nome);
    printf("Bem-vindo, %s", nome);
    return 0;
    }
###############################################################
08.  

    #include <stdio.h>

    char main()
    {
    char caracto[0];
    printf("Informa um caracter: ");
    scanf("%c", &caracto[0]);
    printf("Foi escolhido o: [%s]", caracto);
    return 0;
    }
###############################################################
09. 

    #include <stdio.h>

    char main()
    {
    char caracto[0];
    printf("Informa um caracter: ");
    scanf("%s", &caracto[0]);
    printf("Foi escolhido o: [%s]", caracto);
    return 0;
    }
    #include <stdio.h>

    int main() {
    char entrada[4];

    printf("Digite três caracteres: ");
    scanf("%s", entrada); 
    char temp = entrada[0];
    entrada[0] = entrada[1];
    entrada[1] = temp;

    printf("Resultado (trocado): %s\n", entrada);

    return 0;
    }
