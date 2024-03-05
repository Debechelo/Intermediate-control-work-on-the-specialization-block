public class ToyStoreApp {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();

        // Добавление игрушек
        toyStore.addOrUpdateToy(new Toy(1, "Мяч", 10, 20));
        toyStore.addOrUpdateToy(new Toy(2, "Кукла", 15, 30));
        toyStore.addOrUpdateToy(new Toy(3, "Машинка", 20, 50));

        // Розыгрыш и запись призовой игрушки в файл
        Toy chosenToy = toyStore.chooseToy();
        if (chosenToy != null) {
            toyStore.writeToFile(chosenToy, "prizes.txt");
            System.out.println("Поздравляем! Вы выиграли " + chosenToy.getName());
        } else {
            System.out.println("К сожалению, призовые игрушки закончились.");
        }
    }
}