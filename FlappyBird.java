import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Random;

public class FlappyBird extends JPanel implements ActionListener {
    private int birdY = 150;
    private int birdX = 50;
    private int gravity = 1;
    private int score = 0;
    private boolean gameOver = false;
    private ArrayList<Rectangle> pipes;
    private Timer timer;

    public FlappyBird() {
        pipes = new ArrayList<>();
        timer = new Timer(20, this);
        timer.start();
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_SPACE && !gameOver) {
                    birdY -= 30; // jump
                }
            }
        });
        setFocusable(true);
        generatePipes();
    }

    private void generatePipes() {
        Random rand = new Random();
        int pipeHeight = rand.nextInt(200) + 50;
        pipes.add(new Rectangle(400, 0, 50, pipeHeight));
        pipes.add(new Rectangle(400, pipeHeight + 100, 50, 600 - pipeHeight - 100));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.CYAN);
        g.fillRect(0, 0, getWidth(), getHeight());

        g.setColor(Color.YELLOW);
        g.fillRect(birdX, birdY, 20, 20);

        g.setColor(Color.GREEN);
        for (Rectangle pipe : pipes) {
            g.fillRect(pipe.x, pipe.y, pipe.width, pipe.height);
        }

        g.setColor(Color.BLACK);
        g.drawString("Score: " + score, 10, 20);

        if (gameOver) {
            g.setColor(Color.RED);
            g.drawString("Game Over!", getWidth() / 2 - 30, getHeight() / 2);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (!gameOver) {
            birdY += gravity;

            // Move pipes
            for (Rectangle pipe : pipes) {
                pipe.x -= 5;
            }

            // Check for collision
            for (Rectangle pipe : pipes) {
                if (pipe.intersects(new Rectangle(birdX, birdY, 20, 20))) {
                    gameOver = true;
                }
            }

            // Remove off-screen pipes and increase score
            if (!pipes.isEmpty() && pipes.get(0).x < -50) {
                pipes.remove(0);
                pipes.remove(0);
                score++;
                generatePipes();
            }

            // Check for ground collision
            if (birdY > getHeight() - 20) {
                gameOver = true;
            }

            repaint();
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Flappy Bird");
        FlappyBird game = new FlappyBird();
        frame.add(game);
        frame.setSize(400, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}