# Nome do executável
TARGET = programa

# Compilador
CC = gcc

# Flags do compilador (por exemplo, -Wall para mostrar avisos, -g para debug)
CFLAGS = -Wall -g

# Bibliotecas extras (como a matemática -lm)
LIBS = -lm

# Arquivos fonte e objetos
SRCS = metodo-bisseccao.c
OBJS = $(SRCS:.c=.o)

# Regra padrão
all: $(TARGET)

# Regra para gerar o executável
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) $(LIBS)

# Regra para gerar arquivos .o
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Limpar arquivos compilados
clean:
	rm -f $(OBJS) $(TARGET)

# Para recompilar completamente
rebuild: clean all
