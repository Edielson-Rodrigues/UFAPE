#ifndef FUNCOES_GERAIS.h
#define FUNCOES_GERAIS.h

extern int entradasValidasGestao[] = {0, 1, 2, 3, 4};
extern int entradasValidasFuncoes[] = {0, 1, 2, 3, 4, 5};

// Valida se a entrada foi válida
// -> tipo = 0 (Gestão)
// -> tipo = 1 (ações/funções)
int validarEntrada(int entrada, int tipo);

#endif
