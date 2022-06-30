package com.example.myapplication_cookbook;

public class Recipe {
    public String name;
    public String Text;
    public String[] IngredientArray;

    public Recipe(String name, String text, String[] ingredientArray) {
        this.name = name;
        Text = text;
        IngredientArray = ingredientArray;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getText() {
        return Text;
    }

    public void setText(String text) {
        Text = text;
    }

    public String[] getIngredientArray() {
        return IngredientArray;
    }

    public void setIngredientArray(String[] ingredientArray) {
        IngredientArray = ingredientArray;
    }
}

