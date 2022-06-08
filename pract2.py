foreach( pixel in 8bit_picture ) //для каждого пикселя
{
      if( I(pixel) > Threshold )
      {
          I(pixel) = Белый;
          Error = I(pixel) - Белый;
      }
      else
      {
          I(pixel) = Черный;
          Error = I(pixel) - Черный;
      }
      I(pixel.right)+= 7/16 * Error;
      I(pixel.down_right)+= 1/16 * Error;
      I(pixel.down)+= 5/16 * Error;
      I(pixel.down_left)+= 3/16 * Error;
}