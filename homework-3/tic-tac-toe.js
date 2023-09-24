const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");
const readlineInterface = readline.createInterface({
  input: stdin,
  output: stdout,
});

class Game {
  static #playerSymbol = "x";
  static #programSymbol = "o";
  static #emptySymbol = "-";
  static #size = 3;
  static #coordinates = Array.from({ length: this.#size }, (_, i) => i + 1);

  constructor(readlineInterface) {
    this.#readlineInterface = readlineInterface;
  }

  #readlineInterface;

  #gameboard = Array.from({ length: Game.#size }, () => {
    return new Array(Game.#size).fill(Game.#emptySymbol);
  });

  get #lines() {
    return [
      ...this.#gameboard,
      ...this.#gameboard[0].map((_, index) => {
        return this.#gameboard.map((line) => line[index]);
      }),
      this.#gameboard.map((line, index) => line[index]),
      this.#gameboard.map((line, index) => line[line.length - index - 1]),
    ];
  }

  #hasSomeoneWon(querySymbol) {
    return this.#lines
      .map((line) => line.every((symbol) => symbol === querySymbol))
      .some((boolean) => boolean);
  }

  #hasProgramWon() {
    return this.#hasSomeoneWon(Game.#programSymbol);
  }

  #hasPlayerWon() {
    return this.#hasSomeoneWon(Game.#playerSymbol);
  }

  #isGameOver() {
    return this.#hasProgramWon() || this.#hasPlayerWon();
  }

  #areCoordinatesCorrect(x, y) {
    return Game.#coordinates.includes(x) && Game.#coordinates.includes(y);
  }

  #isSpaceEmpty(x, y) {
    return this.#gameboard[x - 1][y - 1] === Game.#emptySymbol;
  }

  #printGameboard() {
    const firstLine =
      Game.#coordinates.map((digit) => `\t${digit}:`).join("") + "\n";

    const restOfBoard = this.#gameboard
      .map((line, index) => `${index + 1}:\t${line.join("\t")}`)
      .join("\n");

    console.log(firstLine + restOfBoard);
  }

  #makePlayerMove(x, y) {
    this.#gameboard[x - 1][y - 1] = Game.#playerSymbol;
  }

  #makeProgramMove() {
    const availableSpaces = this.#gameboard.reduce((lineAcc, line, x) => {
      const reducedLine = line.reduce((symbolAcc, symbol, y) => {
        if (symbol === Game.#emptySymbol) {
          return [...symbolAcc, [x, y]];
        }

        return symbolAcc;
      }, []);

      return [...lineAcc, ...reducedLine];
    }, []);

    const [x, y] =
      availableSpaces[Math.floor(Math.random() * availableSpaces.length)];

    this.#gameboard[x][y] = Game.#programSymbol;
  }

  async play() {
    if (this.#isGameOver()) {
      console.log("Игра закончена!");
      return;
    }

    this.#printGameboard();

    while (!this.#isGameOver()) {
      const answer = await this.#readlineInterface.question(
        "\nВведите через запятую номер строки и столбца или команду q для выхода из программы:\n"
      );

      if (answer === "q") {
        console.log("\nДо встречи! :3");
        break;
      }

      const [x, y] = answer.split(",").map((str) => Number(str));

      if (this.#areCoordinatesCorrect(x, y)) {
        if (!this.#isSpaceEmpty(x, y)) {
          console.log("\nЭта клетка уже занята. Попробуйте ещё раз!");
          continue;
        }

        this.#makePlayerMove(x, y);
        this.#printGameboard();

        if (this.#hasPlayerWon()) {
          console.log("\nПоздравляю, вы выиграли!");
          break;
        }

        this.#makeProgramMove();
        console.log("\nХод программы:");
        this.#printGameboard();

        if (this.#hasProgramWon()) {
          console.log("\nК сожалению, вы проиграли... :с");
          break;
        }
      } else {
        console.log("\nНеверно введённые данные... Попробуйте ещё раз!");
      }
    }

    this.#readlineInterface.close();
  }
}

const game = new Game(readlineInterface);
game.play();