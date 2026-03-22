global verify_signature

section .text

verify_signature:
	; rdi = token pointer(ignored for now)
	; rsi = secret pointer (ignored for now)

	;simluate "valid token"
	mov rax, 1
	ret
