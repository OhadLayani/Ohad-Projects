package com.example.myapplication_cookbook;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import com.google.firebase.database.FirebaseDatabase;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link ActivityReadFrag#newInstance} factory method to
 * create an instance of this fragment.
 */
public class ActivityReadFrag extends Fragment {
    private static final String[] RecipeTypes=new String[]{
            "Dessert","Middle eastern","Morning","Asian","Italian"
    };
    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    public ActivityReadFrag() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment ActivityReadFrag.
     */
    // TODO: Rename and change types and number of parameters
    public static ActivityReadFrag newInstance(String param1, String param2) {
        ActivityReadFrag fragment = new ActivityReadFrag();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_activity_read, container, false);
        Button button = view.findViewById(R.id.EditRecipe);
        AutoCompleteTextView DropDown = view.findViewById(R.id.readRecipeType);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(getActivity(), android.R.layout.simple_list_item_1, RecipeTypes);
        DropDown.setAdapter(adapter);
        EditText IngredientTextField=view.findViewById(R.id.Ingredientlist);
        ImageView imageView =view.findViewById(R.id.Reciperead);
       // EditText mTextField=view.findViewById(R.id.Reciperead);
        AutoCompleteTextView RecipeFolder=view.findViewById(R.id.readRecipeType);
        EditText RecipeName=view.findViewById(R.id.Recipe_Nameread);
        String RecipeText= (String) MainActivity.RecipeTextBundle.get("Recipe");
        String Foldername=(String) MainActivity.RecipeTypeBundle.get("Recipetype") ;
        String Recipename=(String)MainActivity.RecipeNameBundle.get("Recipename");
        String RecipeIngr=(String)MainActivity.RecipeingredientsBundle .get("Ingredients:");
        System.out.println(RecipeIngr);


        imageView.setImageBitmap(texttobitmap(RecipeText));
       // mTextField.setText(RecipeText);
        RecipeFolder.setText(Foldername);
        RecipeName.setText(Recipename);
        IngredientTextField.setText(RecipeIngr);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Navigation.findNavController(view).navigate(R.id.action_activityReadFrag_to_activityFragment);


            }

        });


        return view;
    }
    public Bitmap texttobitmap(String Text){
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        paint.setTextSize(6);
        paint.setColor(Color.BLACK);
        paint.setTextAlign(Paint.Align.LEFT);
        Float baseline =-paint.ascent();
        int width=(int)(paint.measureText(Text)+0.5f);
        int height  =(int)(baseline+paint.descent() +0.5f);
        Bitmap image =Bitmap.createBitmap(width,height,Bitmap.Config.ARGB_8888);
        Canvas canvas=new Canvas(image);
        canvas.drawText(Text,0,baseline,paint);

        return image;
    }//not functioning properly? find how to save proper image.
}
