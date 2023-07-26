/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

__attribute__((naked))
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    __asm__(".intel_syntax noprefix;\
    push rbx;\
    sub rsp, 0x40;\
    mov qword ptr [rsp+0x10], rdi;\
    mov dword ptr [rsp+0x18], esi;\
    mov dword ptr [rsp+0x20], edx;\
    mov qword ptr [rsp+0x28], rcx;\
    mov rdi, 8;\
    call malloc;\
    mov qword ptr [rsp+0x30], rax;\
    xor r8, r8;\
    outerloop:\
    mov r9, r8;\
    add r9, 1;\
    innerloop:\
    mov rbx, qword ptr [rsp+0x10];\
    xor rax, rax;\
    lea rbx, [rbx+r8*4];\
    add eax, dword ptr [rbx];\
    mov rbx, qword ptr [rsp+0x10];\
    lea rbx, [rbx+r9*4];\
    add eax, dword ptr [rbx];\
    mov ebx, dword ptr [rsp+0x20];\
    cmp ebx, eax;\
    jne continue;\
    mov rax, qword ptr [rsp+0x30];\
    mov dword ptr [rax], r8d;\
    lea rax, [rax+4];\
    mov dword ptr [rax], r9d;\
    mov rax, qword ptr [rsp+0x28];\
    mov dword ptr [rax], 0x2;\
    jmp leave;\
    continue:\
    inc r9;\
    cmp r9d, dword ptr [rsp+0x18];\
    jle innerloop;\
    inc r8;\
    cmp r8d, dword ptr [rsp+0x18];\
    jle outerloop;\
    leave:\
    mov rax, qword ptr [rsp+0x30];\
    add rsp, 0x40;\
    pop rbx;\
    ret;\
    .att_syntax;");
}

int main() {}