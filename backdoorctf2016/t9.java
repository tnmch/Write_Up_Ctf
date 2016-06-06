import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class t9 {
        public static void main(String[] args) 
        {  BufferedReader inputReader=new java.io.BufferedReader(new InputStreamReader(System.in));
           String inputCode="";
           System.out.println("T9 SMS MODE Decoder");
           System.out.println("\nEnter the Value You Want to Press ");
           try 
           {
                inputCode=inputReader.readLine();
           }
           catch(IOException e)
           {
                System.out.println("IO Exception");
           }

           System.out.println(t9.decode(inputCode));        
         }
    
         private static char [][] keyPadCharSet= 
         {
            {' '},
            {'.',',','\'','?','!','\"','-','(',')'},
            {'a','b','c'},
            {'d','e','f'},
            {'g','h','i'},
            {'j','k','l'},
            {'m','n','o'},
            {'p','q','r','s'},
            {'t','u','v'},
            {'w','x','y','z'},
          };
    
          public static String decode(String inputCode)
          {
                StringBuilder outputString=new StringBuilder("");
                char[] inputCodeCharArray=inputCode.toCharArray();
                int len=inputCodeCharArray.length;
                int count=0;

                for(int i=0;i<len;i++) {
                char currentChar=inputCodeCharArray[i];
                char nextChar;

                if((i+1)!=len)  
                    nextChar=inputCodeCharArray[i+1];
                else
                    nextChar='\0';

                if(currentChar==nextChar)
                    count++;    
                else 
                {
                
                     if(currentChar!=' ') 
                     {  if(Character.isDigit(currentChar)) 
                        {    
                            int temp=Integer.parseInt(String.valueOf(currentChar)); 
                            count=count%keyPadCharSet[temp].length; 
                            char outputChar=keyPadCharSet[temp][count]; 
                            outputString.append(outputChar);    
                         }
                         else 
                         {   outputString=new StringBuilder("Please Enter Numerical value Only");
                              break;  
                         }
                      }
                      count=0; 
                  }
        }
        return outputString.toString(); 
    }
    
}
