global asm_calcular_gini
section .text

asm_calcular_gini:
    ; se guarda la posicion del base counter de c
    push rbp        
    mov rbp, rsp    

    ; se convierte el float en XMM0 a int y lo mueve al EAX
    cvttss2si eax, xmm0
    
    ; se incrementa 1 al EAX
    inc eax

    ; se devuelve la posicion de memoria (se desarma el stack frame)
    mov rsp, rbp    
    pop rbp         

    ret