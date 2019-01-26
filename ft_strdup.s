	extern _malloc
	extern _ft_strlen
	extern _ft_memcpy
	global _ft_strdup
	default rel
	section .text
_ft_strdup:
	call _ft_strlen
	push rdi 					;rdi const char*
	mov rdi, rax				;rax ft_strlen ret
	add rdi, 1					;rdi == rax + 1
	push rdi					;save size
	mov rdi, [rsp]				;get size from stack
	sub rsp, 8					;align
	call _malloc
	add rsp, 8					;restore
	pop rdx						;put size in rdx
	pop rsi						;put source in rsi
	cmp rax, 0					;malloc == NULL?
	jz END						;if NULL return NULL
	mov rdi, rax				;put malloc ret in rdi
	call _ft_memcpy
END:
	ret
