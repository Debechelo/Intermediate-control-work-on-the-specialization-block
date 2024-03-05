import java.io.*;
import java.util.*;

class ToyStore {
    private List<Toy> toys;

    public ToyStore() {
        toys = new ArrayList<>();
    }

    public void addOrUpdateToy(Toy toy) {
        for (Toy t : toys) {
            if (t.getId() == toy.getId()) {
                t.setFrequency(toy.getFrequency());
                return;
            }
        }
        toys.add(toy);
    }

    public Toy chooseToy() {
        Random rand = new Random();
        double totalFrequency = toys.stream().mapToDouble(Toy::getFrequency).sum();
        double randValue = rand.nextDouble() * totalFrequency;

        double currentFreq = 0;
        for (Toy toy : toys) {
            currentFreq += toy.getFrequency();
            if (randValue <= currentFreq) {
                Toy chosenToy = new Toy(toy.getId(), toy.getName(), 1, toy.getFrequency());
                toy.setQuantity(toy.getQuantity() - 1);
                return chosenToy;
            }
        }
        return null;
    }

    // Метод записи призовой игрушки в файл
    public void writeToFile(Toy toy, String filename) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename, true))) {
            writer.write("ID: " + toy.getId() + ", Название: " + toy.getName() + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}