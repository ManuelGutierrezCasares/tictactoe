import pyautogui;
import time;

pathVSCode = 'E:/ManuBot/tictactoe_bot/scr/vscode.png';
pathChrome = 'E:/ManuBot/tictactoe_bot/scr/chrome.png';
pathChromeTabTictactoe = 'E:/ManuBot/tictactoe_bot/scr/chrome_tab.png';
pathTictactoePlay =  'E:/ManuBot/tictactoe_bot/scr/tictactoe_play.png';
pathTictactoePve = 'E:/ManuBot/tictactoe_bot/scr/tictactoe_pve.png';
pathTictactoeGameMode = 'E:/ManuBot/tictactoe_bot/scr/tictactoe_gamemode.png';

#Board
pathTictactoeBoard1x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_1x1.png';
pathTictactoeBoard1x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_1x2.png';
pathTictactoeBoard1x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_1x3.png';
pathTictactoeBoard2x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_2x1.png';
pathTictactoeBoard2x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_2x2.png';
pathTictactoeBoard2x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_2x3.png';
pathTictactoeBoard3x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_3x1.png';
pathTictactoeBoard3x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_3x2.png';
pathTictactoeBoard3x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/board_tiles/tictactoe_board_3x3.png';

#Enemy
pathTictactoeEnemy1x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_1x1.png';
pathTictactoeEnemy1x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_1x2.png';
pathTictactoeEnemy1x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_1x3.png';
pathTictactoeEnemy2x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_2x1.png';
pathTictactoeEnemy2x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_2x2.png';
pathTictactoeEnemy2x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_2x3.png';
pathTictactoeEnemy3x1 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_3x1.png';
pathTictactoeEnemy3x2 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_3x2.png';
pathTictactoeEnemy3x3 = 'E:/ManuBot/tictactoe_bot/scr/tiles/enemy_tiles/tictactoe_enemy_3x3.png';


def main():

    #Initialize PyAutoGUI
    pyautogui.FAILSAFE = True


    countdownCounter = 1;
    #Countdown to start
    #print("Starting...")
    #for i in range (0, 10):
    #    print (countdownCounter);
    #    countdownCounter +=1;
    #    time.sleep(.3);
    #print ("go");

    """
    #Move Mouse to Notepad (Fixed)
    pyautogui.moveTo(1892,304);
    """

    def cosaRara():
        print("Cosa Rara");


    cosaRara();

    entrarJuego();
    seleccionarOpcion();
    juegoGanador();    
    
    
    #Return to VSCode
    vscode = pyautogui.locateOnScreen(pathVSCode);
    pyautogui.moveTo(vscode);
    pyautogui.leftClick();
    
    #End
    print("End");


def entrarJuego ():
    #Move Mouse to Chrome (Dynamic)
    chrome = pyautogui.locateOnScreen(pathChrome);
    pyautogui.moveTo(chrome);
    pyautogui.leftClick();
    time.sleep(5);

    #Move Mouse to ChromeTabTictactoe (Dynamic)
    chromeTab = pyautogui.locateOnScreen(pathChromeTabTictactoe,confidence=0.9);
    pyautogui.moveTo(chromeTab);
    pyautogui.leftClick();
    time.sleep(5);
    
    #Refresh ChromeTab
    pyautogui.press('f5');
    time.sleep(15);

    #Move Mouse to Play (Dynamic)
    play = pyautogui.locateOnScreen(pathTictactoePlay);
    pyautogui.moveTo(play);
    pyautogui.leftClick();
    time.sleep(5);


def seleccionarOpcion ():
    #Move Mouse to Select option Pve (Dynamic)
    pve = pyautogui.locateOnScreen(pathTictactoePve);
    pyautogui.moveTo(pve);
    pyautogui.leftClick();
    time.sleep(5);

    #Move Mouse to Select option GameMode (Dynamic)
    gameMode = pyautogui.locateOnScreen(pathTictactoeGameMode);
    pyautogui.moveTo(gameMode);
    pyautogui.leftClick();
    time.sleep(5);
    


def juegoGanador():
    #Select 1x1 tile from board (Dynamic)
    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x1);
    pyautogui.click(selectTile);  
    time.sleep(5);

    #Ganador seguro si elige 3x3
    if pyautogui.locateOnScreen(pathTictactoeEnemy3x3):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
        pyautogui.click(selectTile);
        time.sleep(5);

        if pyautogui.locateOnScreen(pathTictactoeEnemy2x1):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
            pyautogui.click(selectTile);
            time.sleep(5);

            if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                pyautogui.click(selectTile);
                time.sleep(5);
                print("SALIDA 1 eligió 3x3");
            else:
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x2);
                pyautogui.click(selectTile);
                time.sleep(5);
                print ("SALIDA 2 eligió 3x3");
    
    #Ganador seguro si elige 3x1
    if pyautogui.locateOnScreen(pathTictactoeEnemy3x1):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
        pyautogui.click(selectTile);
        time.sleep(5);

        if pyautogui.locateOnScreen(pathTictactoeEnemy2x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
            pyautogui.click(selectTile);
            time.sleep(5);

            if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                pyautogui.click(selectTile);
                time.sleep(5);
                print("SALIDA 1 eligió 3x1");
            else:
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x3);
                pyautogui.click(selectTile);
                time.sleep(5);
                print ("SALIDA 2 eligió 3x1");
        #########elif 
    #Ganador seguro si elige 1x3
    if pyautogui.locateOnScreen(pathTictactoeEnemy1x3):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
        pyautogui.click(selectTile);
        time.sleep(5);

        if pyautogui.locateOnScreen(pathTictactoeEnemy2x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
            pyautogui.click(selectTile);
            time.sleep(5);

            if pyautogui.locateOnScreen(pathTictactoeBoard2x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
                pyautogui.click(selectTile);
                time.sleep(5);
                print("SALIDA 1 eligió 3x1");
            else:
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
                pyautogui.click(selectTile);
                time.sleep(5);
                print ("SALIDA 2 eligió 3x1");
    
    #Ganador seguro si elige 2x2 - y esquina luego
    if pyautogui.locateOnScreen(pathTictactoeEnemy2x2):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
        pyautogui.click(selectTile);
        time.sleep(5);
        if pyautogui.locateOnScreen(pathTictactoeEnemy1x3):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard2x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
                pyautogui.click(selectTile);
                time.sleep(5);
            else:
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
                pyautogui.click(selectTile);
                time.sleep(5);
        elif pyautogui.locateOnScreen(pathTictactoeEnemy3x1):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                pyautogui.click(selectTile);
                time.sleep(5);
            else:
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x3);
                pyautogui.click(selectTile);
                time.sleep(5);
    
    #Ganador seguro si elige 2x2 - y laterales luego
    if pyautogui.locateOnScreen(pathTictactoeEnemy2x2):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
        pyautogui.click(selectTile);
        time.sleep(5);
        #Lateral Izquierdo 2x1
        if pyautogui.locateOnScreen(pathTictactoeEnemy2x1):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x3);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeEnemy1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
                if pyautogui.locateOnScreen(pathTictactoeBoard3x2):
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
                    pyautogui.click(selectTile);
                    time.sleep(5); 
                else:
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                    pyautogui.click(selectTile);
                    time.sleep(5);
        #Lateral Derecho 2x3
        elif pyautogui.locateOnScreen(pathTictactoeEnemy2x3):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
                pyautogui.click(selectTile);
                time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeEnemy1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                pyautogui.click(selectTile);
                time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
                pyautogui.click(selectTile);
                time.sleep(5); 
            elif pyautogui.locateOnScreen(pathTictactoeEnemy3x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
                pyautogui.click(selectTile);
                time.sleep(5);
        #Lateral Arriba 1x2
        elif pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard3x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeEnemy3x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
                pyautogui.click(selectTile);
                time.sleep(5);
                if pyautogui.locateOnScreen(pathTictactoeBoard2x3):
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x3);
                    pyautogui.click(selectTile);
                    time.sleep(5); 
                else:
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
                    pyautogui.click(selectTile);
                    time.sleep(5);
        #Lateral Abajo 3x2
        elif pyautogui.locateOnScreen(pathTictactoeEnemy3x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeEnemy1x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
                if pyautogui.locateOnScreen(pathTictactoeBoard2x1):
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
                    pyautogui.click(selectTile);
                    time.sleep(5); 
                else:
                    selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x3);
                    pyautogui.click(selectTile);
                    time.sleep(5);
        
    #Ganador seguro si elige lateral izquierdo de una
    if pyautogui.locateOnScreen(pathTictactoeEnemy2x1):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
        pyautogui.click(selectTile);
        time.sleep(5);
        #
        if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
            pyautogui.click(selectTile);
            time.sleep(5);
        elif pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x2);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard3x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeBoard3x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
                pyautogui.click(selectTile);
                time.sleep(5);
    #Ganador seguro si elige lateral abajo de una
    if pyautogui.locateOnScreen(pathTictactoeEnemy3x2):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
        pyautogui.click(selectTile);
        time.sleep(5);
        #
        if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
            pyautogui.click(selectTile);
            time.sleep(5);
        elif pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x2);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard3x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeBoard3x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
                pyautogui.click(selectTile);
                time.sleep(5);
    #Ganador seguro si elige lateral derecho de una
    if pyautogui.locateOnScreen(pathTictactoeEnemy2x3):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x3);
        pyautogui.click(selectTile);
        time.sleep(5);
        #
        if pyautogui.locateOnScreen(pathTictactoeBoard1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard1x2);
            pyautogui.click(selectTile);
            time.sleep(5);
        elif pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x2);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard3x1):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeBoard3x3):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
                pyautogui.click(selectTile);
                time.sleep(5);
    #Ganador seguro si elige lateral arriba de una
    if pyautogui.locateOnScreen(pathTictactoeEnemy1x2):
        selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x1);
        pyautogui.click(selectTile);
        time.sleep(5);
        if pyautogui.locateOnScreen(pathTictactoeBoard2x1):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x1);
            pyautogui.click(selectTile);
            time.sleep(5);
        elif pyautogui.locateOnScreen(pathTictactoeEnemy2x1):
            selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x3);
            pyautogui.click(selectTile);
            time.sleep(5);
            if pyautogui.locateOnScreen(pathTictactoeBoard2x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard2x2);
                pyautogui.click(selectTile);
                time.sleep(5);
            elif pyautogui.locateOnScreen(pathTictactoeBoard3x2):
                selectTile = pyautogui.locateOnScreen(pathTictactoeBoard3x2);
                pyautogui.click(selectTile);
                time.sleep(5);

    
    
    




if __name__ == "__main__":
    main()