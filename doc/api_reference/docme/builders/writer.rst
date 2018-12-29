=========
writer.py
=========

Location Path: 
    *docme/builders/writer.py*

class :class:`DocWriter<docme.builders.writer.DocWriter>`
---------------------------------------------------------

.. py:class:: docme.builders.writer.DocWriter(object)
            
        | **Inherits From:** 
        |   :class:`object<__builtin__.object>`
    
    .. py:method:: docme.builders.writer.DocWriter.__init__(self, to_doc_dirs, external_docs)
    
    
    .. py:method:: docme.builders.writer.DocWriter.generate_path_modules(cls, dirname, path)
    
            Generate given path module objects - only py files are watched.
            
            :param dirname: the root dirname of the docs.
            :type dirname: str
            :param path: the path to generate doc from.
            :type path: str
            
            :returns: list of File objects.
            :rtype: list
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.create_rst_files(cls, current_folder, files)
    
            Make rst files from the files parameter.
            
            .. note:: Creates missing directories.
            
            :param current_folder: path of the current folder to write the doc into.
            :type current_folder: str
            :param files: list of File objects - contains the modules to write into the folder.
            :type files: list
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.make_index(cls, path, out_dir, default_title, config, files)
    
            Generate index file to the given path.
            
            :param path: the path of the related folder to make the index of.
            :type path: str
            :param out_dir: the path of the out dir to make the index to.
            :type out_dir: str
            :param default_title: incase there is no doc.yml file in the folder, this title will be chosen.
            :type default_title: str
            :param config: doc.yml file the configures the doc output.
            :type config: dict
            :param files: list of file mount points to add to current index.
            :type files: list
            
            :returns:
            
                      namedtuple contains `module` which is Module object that has the doc in it,
                          and `mount_path` where to mount the current doc relative to `path` root.
            :rtype: File
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.write_files(self, path, files, out_dir, default_title, config)
    
            Write the given files into the given out_dir and create index of them.
            
            :param path: the path of the related folder to make the index of.
            :type path: str
            :param out_dir: the path of the out dir to make the index to and doc files.
            :type out_dir: str
            :param default_title: in-case there is no doc.yml file in the folder, this title will be chosen.
            :type default_title: str
            :param config: doc.yml file the configures the doc output.
            :type config: dict
            :param files: list of File objects to add to write.
            :type files: list
            
            :returns:
            
                      namedtuple contains `module` which is Module object that has the doc in it,
                          and `mount_path` where to mount the current doc relative to `path` root.
            :rtype: File
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.generate_root_path_reference(self, dirname, root, out_dir)
    
            Generate given path sub modules - only folders are watched.
            
            .. note:: this function calls in recursion to `generate_root_path_reference` method.
            
            :param dirname: the dirname of the given root.
            :type dirname: str
            :param root: the path to generate doc from.
            :type root: str
            :param out_dir: the path to generate doc into.
            :type out_dir: str
            
            :returns: list of File objects.
            :rtype: list
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.generate_full_api_reference(self, out_dir)
    
            Generate full api reference from the given doc dirs.
            
            :param out_dir: the path to generate doc into.
            :type out_dir: str
            
            :returns: list of File objects.
            :rtype: list
            
    
    
    
    .. py:method:: docme.builders.writer.DocWriter.generate(self, out_dir)
    
            Generate full doc.
            
            :param out_dir: the path to generate doc into.
            :type out_dir: str
            
            :returns: list of File objects.
            :rtype: list
            
    
    
    

