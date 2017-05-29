//um parser pra arquivos bitmap, lembrar de dissecar e ler, thank you based stackoverflow

/*
»This is how you maually load a bmp file

The bitmap file format: Bitmap file header Bitmap info header palette data Bitmap Dada

so on with the code part, this is our struct we need to create to hold the bitmap file header
*/
#pragma pack(push, 1)

typedef struct tagBITMAPFILEHEADER
{
    WORD bfType;  //specifies the file type
    DWORD bfSize;  //specifies the size in bytes of the bitmap file
    WORD bfReserved1;  //reserved; must be 0
    WORD bfReserved2;  //reserved; must be 0
    DWORD bOffBits;  //species the offset in bytes from the bitmapfileheader to the bitmap bits
}BITMAPFILEHEADER;

#pragma pack(pop)

/*
the bftype field checks to see if you are infact loading a bmp file, and if you are the field should be 0x4D42.

Now we need to create our bitmapinfoheader struct. This holds info about our bitmap(self explainitory).
*/
#pragma pack(push, 1)

typedef struct tagBITMAPINFOHEADER
{
    DWORD biSize;  //specifies the number of bytes required by the struct
    LONG biWidth;  //specifies width in pixels
    LONG biHeight;  //species height in pixels
    WORD biPlanes; //specifies the number of color planes, must be 1
    WORD biBitCount; //specifies the number of bit per pixel
    DWORD biCompression;//spcifies the type of compression
    DWORD biSizeImage;  //size of image in bytes
    LONG biXPelsPerMeter;  //number of pixels per meter in x axis
    LONG biYPelsPerMeter;  //number of pixels per meter in y axis
    DWORD biClrUsed;  //number of colors used by th ebitmap
    DWORD biClrImportant;  //number of colors that are important
}BITMAPINFOHEADER;

#pragma pack(pop)

//Now on to loading our Bitmap

unsigned char *LoadBitmapFile(char *filename, BITMAPINFOHEADER *bitmapInfoHeader)
{
    FILE *filePtr; //our file pointer
    BITMAPFILEHEADER bitmapFileHeader; //our bitmap file header
    unsigned char *bitmapImage;  //store image data
    int imageIdx=0;  //image index counter
    unsigned char tempRGB;  //our swap variable

    //open filename in read binary mode
    filePtr = fopen(filename,"rb");
    if (filePtr == NULL)
        return NULL;

    //read the bitmap file header
    fread(&bitmapFileHeader, sizeof(BITMAPFILEHEADER),1,filePtr);

    //verify that this is a bmp file by check bitmap id
    if (bitmapFileHeader.bfType !=0x4D42)
    {
        fclose(filePtr);
        return NULL;
    }

    //read the bitmap info header
    fread(bitmapInfoHeader, sizeof(BITMAPINFOHEADER),1,filePtr); // small edit. forgot to add the closing bracket at sizeof

    //move file point to the begging of bitmap data
    fseek(filePtr, bitmapFileHeader.bfOffBits, SEEK_SET);

    //allocate enough memory for the bitmap image data
    bitmapImage = (unsigned char*)malloc(bitmapInfoHeader->biSizeImage);

    //verify memory allocation
    if (!bitmapImage)
    {
        free(bitmapImage);
        fclose(filePtr);
        return NULL;
    }

    //read in the bitmap image data
    fread(bitmapImage,bitmapInfoHeader->biSizeImage,filePtr);

    //make sure bitmap image data was read
    if (bitmapImage == NULL)
    {
        fclose(filePtr);
        return NULL;
    }

    //swap the r and b values to get RGB (bitmap is BGR)
    for (imageIdx = 0;imageIdx < bitmapInfoHeader->biSizeImage;imageIdx+=3) // fixed semicolon
    {
        tempRGB = bitmapImage[imageIdx];
        bitmapImage[imageIdx] = bitmapImage[imageIdx + 2];
        bitmapImage[imageIdx + 2] = tempRGB;
    }

    //close file and return bitmap iamge data
    fclose(filePtr);
    return bitmapImage;
}

/*

BITMAPINFOHEADER bitmapInfoHeader;
unsigned char *bitmapData;

esse trecho aqui é uma sugestão de como fazer um dump dum bmp pra uma matriz.
a ideia é dumpar o bitmap em uma matriz de maneira simplificada, tipo dar um
parse em cada bit da imagem, separar a cor e determinar o que é parede e o 
que é caminho a ser percorrido.


typedef struct __attribute__((__packed__)) {
    unsigned char  b;
    unsigned char  g;
    unsigned char  r;
} IMAGE;

int main(void) {
    FILEHEADER fh;
    INFOHEADER ih;
    FILE *img = fopen("pic.bmp", "rb");
    fread(&fh, sizeof(unsigned char), sizeof(FILEHEADER), img);
    fread(&ih, sizeof(unsigned char), sizeof(INFOHEADER), img);

    IMAGE im[ih.width][ih.height];
    fseek(img, fh.imageDataOffset, 0);
    int i, j;
    for (i = ih.height-1; i >= 0; i--) {
        for (j = 0; j < ih.width; j++) {
            fread(&im[i][j], sizeof(unsigned char), sizeof(IMAGE), img);
            printf("%x%x%x ", im[i][j].r, im[i][j].g, im[i][j].b);
        }
        printf("\n");
    }
    printf("w = %d, h = %d\n", ih.width, ih.height);
}


*/
