#include <iostream>
#include <vector>

bool flipping(int piece, int row, int col, int table[8][8])
{
    bool isValid = false;
    //iterates and check if this move is flip (if there's the same color at somewhere in the line) 
    //if true; flip
    for (int i=row-1; i>-1; i--){ //up
        if (table[i][col]==piece){
            for(int j=row-1; j>i; j--){
                table[j][col]=piece;
                isValid = true;
            }
            break;
        }
        else if(table[i][col]==0) break;

    }
    for (int i=row+1; i<8; i++){ //down
        if (table[i][col]==piece){
            for(int j=row+1; j<i; j++){
                table[j][col]=piece;
                isValid = true;
            }
            break;
        }
        else if(table[i][col]==0) break;
    }


    for (int i=col-1; i>-1; i--){ //left
        if (table[row][i]==piece){
            for(int j=col-1; j>i; j--){
                table[row][j]=piece;
                isValid = true;
            }
            break;
        }
        else if(table[row][i]==0) break;
    }
    for (int i=col+1; i<8; i++){ //right
        if (table[row][i]==piece){
            for(int j=col+1; j<i; j++){
                table[row][j]=piece;
                isValid = true;
            }
            break;
        }
        else if(table[row][i]==0) break;
    }

    for (int i=1; i<8; i++){ //upleft
        int cur_row = row-i;
        int cur_col = col-i;
        if (cur_row<0 || cur_col<0) break;

        if (table[cur_row][cur_col]==piece){
            for (int j=1; j<i; j++){
                table[row-j][col-j]=piece;
                isValid = true;
            }
            break;
        }
        else if (table[cur_row][cur_col]==0) break;
    }
    for (int i=1; i<8; i++){ //upright
        int cur_row = row-i;
        int cur_col = col+i;
        if (cur_row<0 || cur_col>7) break;

        if (table[cur_row][cur_col]==piece){
            for (int j=1; j<i; j++){
                table[row-j][col+j]=piece;
                isValid = true;
            }
            break;
        }
        else if (table[cur_row][cur_col]==0) break;
    }
    for (int i=1; i<8; i++){ //downleft
        int cur_row = row+i;
        int cur_col = col-i;
        if (cur_row>7 || cur_col<0) break;

        if (table[cur_row][cur_col]==piece){
            for (int j=1; j<i; j++){
                table[row+j][col-j]=piece;
                isValid = true;
            }
            break;
        }
        else if (table[cur_row][cur_col]==0) break;
    }
    for (int i=1; i<8; i++){ //downright
        int cur_row = row+i;
        int cur_col = col+i;
        if (cur_row>7 || cur_col>7) break;

        if (table[cur_row][cur_col]==piece){
            for (int j=1; j<i; j++){
                table[row+j][col+j]=piece;
                isValid = true;
            }
            break;
        }
        else if (table[cur_row][cur_col]==0) break;
    }

    return isValid;
}

bool place(int piece, int row, int col, int table[8][8]) //piece: 1=w/-1=b
{
    if (flipping(piece,row,col,table)){
        table[row][col]=piece;
        return true;
    }
    else {
        return false;
    }
}

void printBoard(int table[8][8]) //-1=black, 0=blank, 1=white
{
    std::cout<<"   A B C D E F G H\n";
    for (int row=0; row<8; row++){
        std::cout<<row<<"  ";
        for (auto &i:table[row]){
            switch (i){
                case 0:
                    std::cout<<"- ";
                    break;
                case -1:
                    std::cout<<"O ";
                    break;
                case 1:
                    std::cout<<"0 ";
                    break;
            }
        }
        std::cout<<'\n';
    } 
}

int main(){
    int tiles=60;
    int turn=1; //1=white, -1=black
    bool ending=false;
    std::string coor;

    int table[8][8]={ //0=space, 1=white, 2=black
        { 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 1,-1, 0, 0, 0},
        { 0, 0, 0,-1, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0}
    };

    
    while (!ending){ //1 loop per turn
        printBoard(table);
        std::cout<<'\n';
        if (turn==1) std::cout<<"White's turn : ";
        else std::cout<<"Black's turn : ";

        std::cin>>coor; //A0
        if (coor=="end") break;
        else if (coor=="pass"){
            turn=turn*-1;
            continue;
        }

        int t_row = coor[1]-'0';
        int t_col = coor[0]-'A';

        bool isValidPlace = place(turn,t_row,t_col,table);
        if (isValidPlace){
            std::cout<<"placed\n\n";
            turn=turn*-1;
            tiles--;
            if (tiles<=0) break;
        }
        else {
            std::cout<<"Invalid move, please retry\n\n";
        }
    }

    int white=0;
    int black=0;

    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            if (table[i][j]==1) white++;
            else if (table[i][j]==-1) black++;
        }
    }
    
    printBoard(table);
    if (white>black) std::cout<<"\nWhite wins!!!";
    else if (black>white) std::cout<<"\nBlack wins!!!";
    else std::cout<<"\nDraw!!!";

    std::cout<<"\nWhite : "<<white;
    std::cout<<"\nBlack : "<<black;
}