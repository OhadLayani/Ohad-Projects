package com.example.myapplication_cookbook;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.Navigation;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    public static Bundle RecipeTypeBundle = new Bundle();
    public static Bundle RecipeNameBundle = new Bundle();
    public static Bundle RecipeTextBundle = new Bundle();
    public static Bundle RecipeingredientsBundle = new Bundle();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mAuth = FirebaseAuth.getInstance();

    }
    public void loginFunc(View view) {
        EditText user=findViewById(R.id.editTextTextPersonName2);
        EditText pass=findViewById(R.id.editTextTextPassword);
        String email=user.getText().toString();
        String Password=pass.getText().toString();
        mAuth.signInWithEmailAndPassword(email, Password)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            Toast.makeText(MainActivity.this,"Login Succsessfully managed",Toast.LENGTH_LONG).show();
                            Navigation.findNavController(view).navigate(R.id.action_loginFragment_to_choiceFragmet);

                        } else {
                            Toast.makeText(MainActivity.this,"Login Failed",Toast.LENGTH_LONG).show();
                        }

                        // ...
                    }
                });
    }
    public void RegisterFunc(View view) {
        EditText UserReg=findViewById(R.id.UserNameReg);
        EditText passReg=findViewById(R.id.PassReg);
        EditText EmailReg=findViewById(R.id.EmailReg);
        String UsernameReg=UserReg.getText().toString();
        String PasswordReg=passReg.getText().toString();
        String emailreg= EmailReg.getText().toString();
        mAuth.createUserWithEmailAndPassword(emailreg, PasswordReg)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            Toast.makeText(MainActivity.this,"Register Successfully managed",Toast.LENGTH_LONG).show();


                            User u= new User(UsernameReg,emailreg,PasswordReg);

                            WriteFunc(u);
                            Navigation.findNavController(view).navigate(R.id.action_registrationFragment_to_choiceFragmet);



                        } else {
                            Toast.makeText(MainActivity.this,"Register Successfully Failed",Toast.LENGTH_LONG).show();

                        }

                        // ...
                    }
                });
    }
    public void WriteFunc(User u){
        String id = mAuth.getCurrentUser().getUid();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference("User").child("User :"+id);
        //child id is for writing data to user(id)- sub catagories inside said id (grandchildren)
        //get all data from text layouts in  register


        myRef.setValue(u);

    }
    public void ReadFUnc(View view){
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        String id = mAuth.getCurrentUser().getUid();
        //Read recipe text fragment text fields
        AutoCompleteTextView ReadRecipeFolder=findViewById(R.id.Recipe_Type);
        EditText ReadRecipeName=findViewById(R.id.RecipeNameDropDown);
        String Foldername=ReadRecipeFolder.getText().toString();
        String Recipename=ReadRecipeName.getText().toString();

        System.out.println("Text1");


        DatabaseReference myRef = database.getReference("User").child("User :"+id).child(Foldername).child(Recipename).child("Recipe:") ;

        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
            String recipeText=dataSnapshot.getValue(String.class);



            MainActivity.RecipeTypeBundle.putString("Recipetype",Foldername);
            MainActivity.RecipeNameBundle.putString("Recipename",Recipename);
            MainActivity.RecipeTextBundle.putString("Recipe",recipeText);
                Navigation.findNavController(view).navigate(R.id.action_recipeReadFragment_to_activityReadFrag);


            }

            @Override
            public void onCancelled(DatabaseError error) {
                Toast.makeText(MainActivity.this,"Recipe does not exist in database",Toast.LENGTH_LONG).show();

            }
        });
    }

    public void SaveRecipeFunc(ArrayList<String> ar) {
        AutoCompleteTextView RecipeFolder=findViewById(R.id.NewRecipeType);
        EditText RecipeName=findViewById(R.id.Recipe_Name);
        EditText Recipe=findViewById(R.id.Recipe);
        String Foldername=RecipeFolder.getText().toString();
        String Recipename=RecipeName.getText().toString();
        String RecipeText= Recipe.getText().toString();
        String id = mAuth.getCurrentUser().getUid();

        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference("User").child("User :"+id).child(Foldername).child(Recipename);
        myRef.setValue(Recipename);
        DatabaseReference aRef = database.getReference("User").child("User :"+id).child(Foldername).child(Recipename).child("Recipe:");

        aRef.setValue(RecipeText);
        DatabaseReference ingRef = database.getReference("User").child("User :"+id).child(Foldername).child(Recipename).child("ingredients:");
        ingRef.setValue(ar);

        Toast.makeText(MainActivity.this,"Recipe Saved",Toast.LENGTH_LONG).show();

    }
    public void ReadRecipeIngredients(View view){
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        String id = mAuth.getCurrentUser().getUid();
        AutoCompleteTextView ReadRecipeFolder=findViewById(R.id.Recipe_Type);
        EditText ReadRecipeName=findViewById(R.id.RecipeNameDropDown);
        String Foldername=ReadRecipeFolder.getText().toString();
        String Recipename=ReadRecipeName.getText().toString();
        ArrayList<String> ar = new ArrayList<String>();

        DatabaseReference myRef = (DatabaseReference) database.getReference("User").child("User :"+id).child(Foldername).child(Recipename).child("ingredients:");
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                for (DataSnapshot childSnapshot: dataSnapshot.getChildren()) {
                    String Ingredient = childSnapshot.getValue(String.class);
                    ar.add(Ingredient);
                    System.out.println("1");
                    System.out.println(ar);


                }
                StringBuilder builder = new StringBuilder();
                for (String details : ar) {
                    builder.append(details + "\n");
                    System.out.println(ar);
                    System.out.println("2");

                }
                MainActivity.RecipeingredientsBundle.putString("Ingredients:",builder.toString());
                System.out.println(builder.toString());
                System.out.println(RecipeingredientsBundle);


            }
            @Override
            public void onCancelled(DatabaseError error) {
                Toast.makeText(MainActivity.this,"Recipe does not exist in database",Toast.LENGTH_LONG).show();

            }
        });
    }

    public void getRecipeKeys(View view){
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        String id = mAuth.getCurrentUser().getUid();
        AutoCompleteTextView RecipeFolder=findViewById(R.id.Recipe_Type);
        String Foldername=RecipeFolder.getText().toString();

        DatabaseReference myRef = (DatabaseReference) database.getReference("User").child("User :"+id).orderByChild(Foldername);
        myRef.addValueEventListener(new ValueEventListener() {

            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {


            }
            @Override
            public void onCancelled(DatabaseError error) {

            }
        });
    }

}


