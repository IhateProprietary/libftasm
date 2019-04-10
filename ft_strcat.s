extern _ft_strlen
extern _ft_memcpy
global _ft_strcat
default rel
section .text
_ft_strcat:
	; context
	push rbp
	lea rbp, [rsp]
	;;
	push rdi
	push rsi
	call _ft_strlen
	push rax
	mov rdi, [rsp+8]
	;; align
	sub rsp, 8
	call _ft_strlen
	;; restore
	add rsp, 8
	;; store source len in rdx
	mov rdx, rax
	;; rdi len
	pop rax
	mov rsi, [rsp]
	mov rdi, [rsp+8]
	add rdi, rax
	mov [rdi+rdx], BYTE 0
	call _ft_memcpy
	; leave
	lea rsp, [rbp]
	pop rbp
	ret
