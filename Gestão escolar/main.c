#include <stdio.h>
#include "alunos.h"
#include "funcoesGerais.h"
#include <stdlib.h>

#define TAMANHO_MAXIMO 10

int *totalAlunos;
void main() {
    int manterInteracao = 1, escolhaTipoGestao, escolhaAcao;
    printf("BEM-VINDO\n--------------------------------\n");

    inicializarListaAlunos();

    while (manterInteracao) {
        printf("Escolha uma op��o:\n"
           "1. Gest�o de alunos\n"
           "2. Gest�o de tarefas\n"
           "3. Gest�o de estoque\n"
           "4. Gest�o de biblioteca\n"
           "0. Sair do sistema\n");

        scanf("%d", &escolhaTipoGestao);

        if (!escolhaTipoGestao) {
            printf("At� mais.");
            break;
        } else if (validarEntrada(escolhaTipoGestao, 0)) {
            printf("Escolha uma op��o:\n"
               "1. Inserir\n"
               "2. Listar\n"
               "3. Remover (informe o ID)\n"
               "4. Procurar (informe o ID)\n"
               "5. Tamanho da lista\n"
               "0. Sair\n");

            scanf("%d", &escolhaAcao);

            if (validarEntrada(escolhaAcao, 1)) {
                if (escolhaTipoGestao == 1) {
                    switch (escolhaAcao) {
                    case 1:
                        inserirAluno();
                        break;
                    }
                }
            } else {
                printf("Entrada inv�lida. Voltando ao menu...\n");
            }
        } else {
            printf("Entrada inv�lida.\n");
        }
    }
}


int validarEntrada(int entrada, int tipo) {
    if (tipo == 0) {
        for (int i = 0; i < sizeof(entradasValidasGestao); i++) {
            if (entradasValidasGestao[i] == entrada) {
                return 1;
            }
        }
    } else {
        for (int i = 0; i < sizeof(entradasValidasFuncoes); i++) {
            if (entradasValidasFuncoes[i] == entrada) {
                return 1;
            }
        }
    }
    return 0;
}

void inicializarListaAlunos() {
    totalAlunos = (int *)malloc(sizeof(int));
    *totalAlunos = 0;
    alunosCadastrados = (Aluno *)malloc(TAMANHO_MAXIMO * sizeof(Aluno));
}

int inserirAluno(){
    Aluno aluno;
    // Recebendo as informa��es do aluno
    printf("Informe a matr�cula:\n");
    scanf("%d", &aluno.matricula);

    printf("Informe o nome:\n");
    scanf("%s", &aluno.nome);

    printf("Informe o c�digo da turma:\n");
    scanf("%d", &aluno.codTurma);

    printf("Informe as notas (7 notas):\n");
    for (int i = 0; i < 9; i++) {
        scanf("%f", &aluno.notas[i]);
    }


    printf("Informe a quantidade de faltas:\n");
    scanf("%d", &aluno.faltas);

    if (sizeof(alunosCadastrados) < TAMANHO_MAXIMO) {
        alunosCadastrados[*totalAlunos] = aluno;
        (*totalAlunos)++;
    } else {

    }
}

// tipo 1 -> aluno
int realocarMenoria(int tipo) {
    int novoTamanho = TAMANHO_MAXIMO * 2; // Voc� pode ajustar conforme necess�rio

    // Realoca a mem�ria para a lista de alunos
    alunosCadastrados = (Aluno *)realloc(alunosCadastrados, novoTamanho * sizeof(Aluno));

    // Verifica se a realoca��o foi bem-sucedida
    if (alunosCadastrados == NULL) {
        printf("Erro ao realocar mem�ria para a lista de alunos.\n");
        exit(1); // Sa�da do programa em caso de erro
    }
}
