import java.util.Scanner;

public class velha {
    public static void main(String[] args) {
        char[][] tabuleiro = new char[3][3];
        inicializarTabuleiro(tabuleiro);

        Scanner scanner = new Scanner(System.in);
        char jogadorAtual = 'X';
        boolean jogoAtivo = true;

        System.out.println("Bem-vindo ao Jogo da Velha!");
        exibirTabuleiro(tabuleiro);

        while (jogoAtivo) {
            System.out.println("Jogador " + jogadorAtual + ", faça sua jogada!");
            System.out.print("Digite a linha (0, 1 ou 2): ");
            int linha = scanner.nextInt();
            System.out.print("Digite a coluna (0, 1 ou 2): ");
            int coluna = scanner.nextInt();

            if (linha < 0 || linha > 2 || coluna < 0 || coluna > 2 || tabuleiro[linha][coluna] != '-') {
                System.out.println("Jogada inválida. Tente novamente.");
                continue;
            }
            tabuleiro[linha][coluna] = jogadorAtual;
            exibirTabuleiro(tabuleiro);

            if (verificarVencedor(tabuleiro, jogadorAtual)) {
                System.out.println("Parabéns, Jogador " + jogadorAtual + "! Você venceu!");
                jogoAtivo = false;
            } else if (verificarEmpate(tabuleiro)) {
                System.out.println("O jogo terminou em empate!");
                jogoAtivo = false;
            } else {
                jogadorAtual = (jogadorAtual == 'X') ? 'O' : 'X';
            }
        }

        scanner.close();
        System.out.println("Fim do jogo!");
    }

    public static void inicializarTabuleiro(char[][] tabuleiro) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tabuleiro[i][j] = '-';
            }
        }
    }

    public static void exibirTabuleiro(char[][] tabuleiro) {
        for (char[] linha : tabuleiro) {
            for (char celula : linha) {
                System.out.print(celula + " ");
            }
            System.out.println();
        }
    }

    public static boolean verificarVencedor(char[][] tabuleiro, char jogador) {
        for (int i = 0; i < 3; i++) {
            if (tabuleiro[i][0] == jogador && tabuleiro[i][1] == jogador && tabuleiro[i][2] == jogador) {
                return true;
            }
        }
        for (int i = 0; i < 3; i++) {
            if (tabuleiro[0][i] == jogador && tabuleiro[1][i] == jogador && tabuleiro[2][i] == jogador) {
                return true;
            }
        }
        if (tabuleiro[0][0] == jogador && tabuleiro[1][1] == jogador && tabuleiro[2][2] == jogador) {
            return true;
        }
        if (tabuleiro[0][2] == jogador && tabuleiro[1][1] == jogador && tabuleiro[2][0] == jogador) {
            return true;
        }

        return false;
    }

    public static boolean verificarEmpate(char[][] tabuleiro) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tabuleiro[i][j] == '-') {
                    return false;
                }
            }
        }
        return true;
    }
}
