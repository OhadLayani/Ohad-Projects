package com.example.myapplication_cookbook;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.LinearLayout;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link RecipeReadFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class RecipeReadFragment extends Fragment implements AdapterView.OnItemSelectedListener {

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
    public RecipeReadFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment RecipeReadFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static RecipeReadFragment newInstance(String param1, String param2) {
        RecipeReadFragment fragment = new RecipeReadFragment();
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
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_recipe_read, container, false);
        Button button = view.findViewById(R.id.Load);
        AutoCompleteTextView DropDown = view.findViewById(R.id.Recipe_Type);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(getActivity(), android.R.layout.simple_list_item_1,RecipeTypes);
        DropDown.setAdapter(adapter);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               // Layout.setVisibility(View.VISIBLE);
                //button.setVisibility(View.GONE);
                //EditLayout.setVisibility(View.VISIBLE);
                MainActivity mainActivity = (MainActivity) getActivity();
                mainActivity.ReadRecipeIngredients(view);
                mainActivity.ReadFUnc(view);

            }

        });


        return view;
    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        String choice=adapterView.getItemAtPosition(i).toString();


    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }
}
