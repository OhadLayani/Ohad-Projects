package com.example.myapplication_cookbook;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link ActivityFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class ActivityFragment extends Fragment {


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

    public ActivityFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment ActivityFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static ActivityFragment newInstance(String param1, String param2) {
        ActivityFragment fragment = new ActivityFragment();
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
        View view =  inflater.inflate(R.layout.fragment_activity, container, false);
        ArrayList<String> ar = new ArrayList<String>();

        Button button = view.findViewById(R.id.Save_Recipe);
        AutoCompleteTextView DropDown = view.findViewById(R.id.NewRecipeType);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(getActivity(), android.R.layout.simple_list_item_1,RecipeTypes);
        DropDown.setAdapter(adapter);
        EditText mTextField=view.findViewById(R.id.Recipe);
        EditText RecipeName=view.findViewById(R.id.Recipe_Name);
        CheckBox IngredientCheck=view.findViewById((R.id.IngredientCheckList));

        CheckBox Ingredient1=view.findViewById((R.id.checkBox));
        CheckBox Ingredient2=view.findViewById((R.id.checkBox2));
        CheckBox Ingredient3=view.findViewById((R.id.checkBox3));
        CheckBox Ingredient4=view.findViewById((R.id.checkBox4));
        CheckBox Ingredient5=view.findViewById((R.id.checkBox5));
        CheckBox Ingredient6=view.findViewById((R.id.checkBox6));
        CheckBox Ingredient7=view.findViewById((R.id.checkBox7));
        CheckBox Ingredient8=view.findViewById((R.id.checkBox8));

        String RecipeText= (String) MainActivity.RecipeTextBundle.get("Recipe");
        String Recipename=(String)MainActivity.RecipeNameBundle.get("Recipename");
        LinearLayout ingredientlayout = view.findViewById(R.id.IngredientLayout);

        mTextField.setText(RecipeText);
        RecipeName.setText(Recipename);

        EditText newingredientText=view.findViewById(R.id.NewIngredient);
        LinearLayout addingredientlayout = view.findViewById(R.id.AddingredientLayout);

        Button button1=view.findViewById(R.id.IngredientAddButton);
        Button button2=view.findViewById(R.id.AddButtonVis);

        button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                MainActivity mainActivity = (MainActivity) getActivity();
                mainActivity.SaveRecipeFunc(ar);

            }

        });
        IngredientCheck.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
            if(ingredientlayout.getVisibility()==view.VISIBLE){
                ingredientlayout.setVisibility(View.GONE);
                }
            else{
                ingredientlayout.setVisibility(View.VISIBLE);
            }
            }

        });
        button1.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                if(addingredientlayout.getVisibility()==view.VISIBLE){
                    addingredientlayout.setVisibility(View.GONE);

                }
                else{
                    addingredientlayout.setVisibility(View.VISIBLE);
                }

            }

        });
        button2.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                String nIngredient=newingredientText.getText().toString();
                ar.add(nIngredient);

            }

        });


        Ingredient1.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient1=Ingredient1.getText().toString();
            if(Ingredient1.isChecked()){
                ar.add(ingredient1);
            }else{
                ar.remove(ingredient1);
            }

        }

    });
        Ingredient2.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient2=Ingredient2.getText().toString();
            if(Ingredient2.isChecked()){
                ar.add(ingredient2);
            }else{
                ar.remove(ingredient2);
            }

        }

    });
        Ingredient3.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient3=Ingredient3.getText().toString();
            if(Ingredient3.isChecked()){
                ar.add(ingredient3);
            }else{
                ar.remove(ingredient3);
            }

        }

    });
        Ingredient4.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient4=Ingredient4.getText().toString();
            if(Ingredient4.isChecked()){
                ar.add(ingredient4);
            }else{
                ar.remove(ingredient4);
            }

        }

    });
        Ingredient5.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient5=Ingredient5.getText().toString();
            if(Ingredient5.isChecked()){
                ar.add(ingredient5);
            }else{
                ar.remove(ingredient5);
            }

        }

    });
        Ingredient6.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient6=Ingredient6.getText().toString();
            if(Ingredient6.isChecked()){
                ar.add(ingredient6);
            }else{
                ar.remove(ingredient6);
            }

        }

    });

        Ingredient7.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient7=Ingredient7.getText().toString();
            if(Ingredient7.isChecked()){
                ar.add(ingredient7);
            }else{
                ar.remove(ingredient7);
            }

        }

    });
        Ingredient8.setOnClickListener(new View.OnClickListener() {

        @Override
        public void onClick(View view) {
            String ingredient8=Ingredient8.getText().toString();
            if(Ingredient8.isChecked()){
                ar.add(ingredient8);
            }else{
                ar.remove(ingredient8);
            }

        }

    });
        return view;
    }


}
