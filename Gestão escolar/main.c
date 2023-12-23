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
        printf("Escolha uma opção:\n"
           "1. Gestão de alunos\n"
           "2. Gestão de tarefas\n"
           "3. Gestão de estoque\n"
           "4. Gestão de biblioteca\n"
           "0. Sair do sistema\n");

        scanf("%d", &escolhaTipoGestao);

        if (!escolhaTipoGestao) {
            printf("Até mais.");
            break;
        } else if (validarEntrada(escolhaTipoGestao, 0)) {
            printf("Escolha uma opção:\n"
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
                printf("Entrada inválida. Voltando ao menu...\n");
            }
        } else {
            printf("Entrada inválida.\n");
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
    // Recebendo as informações do aluno
    printf("Informe a matrícula:\n");
    scanf("%d", &aluno.matricula);

    printf("Informe o nome:\n");
    scanf("%s", &aluno.nome);

    printf("Informe o código da turma:\n");
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
    int novoTamanho = TAMANHO_MAXIMO * 2; // Você pode ajustar conforme necessário

    // Realoca a memória para a lista de alunos
    alunosCadastrados = (Aluno *)realloc(alunosCadastrados, novoTamanho * sizeof(Aluno));

    // Verifica se a realocação foi bem-sucedida
    if (alunosCadastrados == NULL) {
        printf("Erro ao realocar memória para a lista de alunos.\n");
        exit(1); // Saída do programa em caso de erro
    }
}
