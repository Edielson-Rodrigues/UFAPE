#ifndef ALUNO_H
#define ALUNO_H

// Declaração da struct aluno
typedef struct {
    int matricula;
    float notas[7];
    char nome[50];
    int codTurma;
    int faltas;
} Aluno;

// importa a lista de alunos, inicialmente com 10 de tamanho]
extern Aluno *alunosCadastrados = NULL;
extern int *totalAlunos;

void inicializarListaAlunos();
int inserirAluno();
void listarAlunos();
int removerAluno(int id);
int buscarAluno(int id);
void tamanhoListaAlunos();


#endif
